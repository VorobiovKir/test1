kThis project contains the main code base of Minimax Website project.

Basic System Requirements:
====================
* PostgreSQL 9.2.x or higher
* Python 2.7 or higher (not 3.x, though!), incl. its header files (i.e. "python2.7-dev")
* Python PIP 1.2.x or higher
* VirtualEnv 1.8.x or higher (optional)
* NodeEnv => Node.js (to have npm available when working on the LESS files, etc.)

How to set up my local development environment?
====================

* Install dependencies using pip:

```sh
pip install -r requirements.txt
```

* Create local development database (use user/pass/db_name from local_settings.py)
- Create user (i.e. role) with password
- Create database (with owner to be the new user)

* Option 1: Create/Update development database as referenced in local settings.

```sh
python manage.py reset_db --router=default --noinput
python manage.py migrate
```

* Option 2: Use production dump to local test data

```sh
python manage.py reset_db --router=default --noinput
pg_restore -U [db_user] -O -1 -n public -d [db_name] --role=[db_user] -h localhost [path_to_dump_file]
python manage.py migrate
```

* Start local development web server (optional, can also be started from within the IDE) providing the user interface.

```sh
python manage.py runserver
```

How to set up the build process for modifications on LESS and Javascript?
====================

* Install necessary node dependencies (taken from package.json)
```sh
npm install
```

* Install necessary bowser dependencies (taken from bowser.json)
```sh
bower install
```

* To generate the JS and CSS for production run
```sh
gulp
```

