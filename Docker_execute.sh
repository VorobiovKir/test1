#!/bin/bash -x
set -e
PROJECT_NAME=minimax-cms

# Delete unused volumes from docker vm from times to times
# docker run --rm -v /var/run/docker.sock:/var/run/docker.sock:ro -v /var/lib/docker:/var/lib/docker martin/docker-cleanup-volumes

# Get into current directory
cd `dirname $0`
rm -rf artifacts
mkdir artifacts

# Build docker image(s)
docker build -t $PROJECT_NAME .

# Run docker container
docker run --rm -v $PWD:/repos:ro -v $PWD/artifacts:/artifacts -e HOST_UID=$(id -u $USER) -e HOST_GID=$(id -g $USER) -t $PROJECT_NAME

set +x
echo "------------------------------------------"
echo "BUILD SUCCEEDED 👍"
echo "------------------------------------------"
