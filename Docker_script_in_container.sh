#!/bin/bash -x
set -e
cp -r /repos /tmp/build
cd /tmp/build

#/etc/init.d/postgresql start

# Create local_settings.py, set module and run tests
cp minimax_site/local_settings.py.bamboo minimax_site/local_settings.py
python manage.py test minimax --noinput

# TODO: Enable again and fix problem on BAMBOO
# Make sure all artifacts can be removed from the outer container
# chown -R "$HOST_UID":"$HOST_GID" /artifacts