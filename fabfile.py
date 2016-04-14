from fabric.api import local

def sync():
    # Welcome message
    print("")
    print("")
    print("Automated synchronization script by Fabric")
    print("=====================================")
    print("")
    print("Use this script for synchronizing staging based on production (using 'fab sync')")
    print("")
    print("Expected settings: ")
    print("GIT remote 'staging' links to staging environment")
    print("GIT remote 'production' links to production environment")
    print("GIT remote 'origin' links to the master repository")
    print("-----------------------------------------------------------------------------")

    confirmation = ''
    while confirmation not in ['yes', 'no']:
        print("Proceed with synchronizing staging using current production data ('yes' or 'no')?")
        confirmation = raw_input()
    print("-----------------------------------------------------------------------------")
    print("")

    # Cancel if no confirmation
    if confirmation == 'no':
        print("Quit by user cancellation")
        return

    # Enable maintenance mode
    local('heroku maintenance:on --remote staging')

    # Synchronize bucket
    local('aws s3 sync s3://minimax-cms-production s3://minimax-cms-staging --delete --profile minimax-cms-sync')

    # Backup production
    local('heroku pg:backups capture -a minimax-cms-production')

    # Backup staging
    local('heroku pg:backups capture -a minimax-cms-staging')

    # Catch URL for production dump
    production_db_url = local('heroku pg:backups public-url -a minimax-cms-production', capture=True)

    # Inject production dump
    local('heroku pg:backups restore "%s" DATABASE_URL -a minimax-cms-staging --confirm minimax-cms-staging' % production_db_url)

    # Disable maintenance mode
    local('heroku maintenance:off --remote staging')


def deploy():
    # Welcome message
    print("")
    print("")
    print("Automated deployment script by Fabric")
    print("=====================================")
    print("")
    print("Use this script for deployment to staging and production (using 'fab deploy')")
    print("This script will deploy your local branch to HEROKU. You will need your")
    print("local environment to be properly configured with the MTG HEROKU environment.")
    print("")
    print("Expected settings: ")
    print("GIT remote 'staging' links to staging environment")
    print("GIT remote 'production' links to production environment")
    print("GIT remote 'origin' links to the master repository")
    print("")
    print("For staging deployment: Make sure that the local branch to be deployed is ")
    print("checked out")
    print("-----------------------------------------------------------------------------")

    # Define variables
    env = ''
    version = ''
    confirmation = ''
    skip_backup = ''

    # Request deployment environment to be selected by user
    print("")
    while env not in ['staging', 'production']:
        print("(1) Please type in deployment environment (i.e. 'staging' or 'production', [Default='staging']):")
        env = raw_input()
        if env == '':
            env = 'staging'
    print("Select value: %s" % env)
    print("-----------------------------------------------------------------------------")
    print("")

    # Get current version from staging
    print("Requesting currently deployed version number from staging environment ...")
    current_staging_version = local('heroku config:get APP_VERSION --remote staging', capture=True)
    print("Found version: %s" % current_staging_version)
    print("-----------------------------------------------------------------------------")
    print("")

    # Make sure to have all tags of the repo and compile the automated version number using git describe
    print("Running 'git fetch --tags' to get full set of tags available in the repo (Needed for auto generated version suggestion)")
    local('git fetch --tags')
    auto_next_staging_version = local('git describe', capture=True)
    print("Auto generated version: %s" % auto_next_staging_version)
    print("-----------------------------------------------------------------------------")
    print("")

    # If staging deployment, we will allow the user to type in a new version
    if env == 'staging':
        print("")
        while version == '' or version == current_staging_version:
            print("(2) Please type in new version number or leave empty to use auto generated version=%s [Current staging version='%s']:" % (auto_next_staging_version, current_staging_version))
            version = raw_input()
            if version == '':
                version = auto_next_staging_version
        print("New version: %s" % version)
        print("-----------------------------------------------------------------------------")
        print("")

        while skip_backup not in ['yes', 'no']:
            print("(2a) Skip backup? (Please type 'yes' or 'no':")
            skip_backup = raw_input()

    # If production deployment only latest version from staging can be deployed
    elif env == 'production':
        version = current_staging_version
    else:
        # This should never be the case
        version = 'undefined'

    print("")
    while confirmation not in ['yes', 'no']:
        if env == 'staging':
            print("(3) Proceed with tagging and deploying currently checkout local branch as '%s' to 'staging' (type 'yes' or 'no')?" % version)
        elif env == 'production':
            print("(3) Proceed with deploying tag '%s' to 'production' (type 'yes' or 'no')?" % version)
        else:
            print "undefined"
        confirmation = raw_input()
    print("Select value: %s" % confirmation)
    print("-----------------------------------------------------------------------------")
    print("")

    # Cancel if no confirmation
    if confirmation == 'no':
        print("Quit by user cancellation")
        return

    # Handle tagging
    if env == 'staging':
        if version != auto_next_staging_version:
            # Create new annotated tag as we deploy to staging and we do not use the auto generated version by GIT
            print("Creating annotated GIT tag, please type in creation comment (i.e. What is the new version about?)")
            comment = raw_input()
            local('git tag -a -m "%s" %s' % (comment, version))
            local('git push origin %s' % version)
        else:
            print("Creating new simple GIT tag")
            local('git tag %s' % version)
            local('git push origin %s' % version)
    elif env == 'production':
        # Make sure that we have all existing tags on board then checkout the tag to be deployed
        print("Checking out existing tag to continue deployment")
        local('git fetch --tags')
        local('git fetch')
        local('git checkout %s' % version)
    else:
        # This should never be the case
        print("Something went wrong as the env seems not to be set")
        return

    # Enable maintenance mode
    local('heroku maintenance:on --remote %s' % env)

    # Set new version number
    local('heroku config:set APP_VERSION=%s --remote %s' % (version, env))

    # Back up and delete oldest one
    if skip_backup != 'yes':
        local('heroku pg:backups capture --remote %s' % env)

    # Push new version
    local('git push %s +HEAD:master' % env)

    # Force migration
    local('heroku run python manage.py migrate --remote %s' % env)

    # Disable maintenance mode
    local('heroku maintenance:off --remote %s' % env)

