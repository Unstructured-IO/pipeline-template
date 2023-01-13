#!/usr/bin/env bash

# Validate the Dockerfile builds in a generated repo, and that the docker
# image may run as the web app or jupyter instance.

set -eux -o pipefail

PROJECT_NAME=testproject


SCRIPT_RELATIVE_DIR=$(dirname "${BASH_SOURCE[0]}")
cd $SCRIPT_RELATIVE_DIR/../pipeline-$PROJECT_NAME

make docker-build
rm -f jupyter.out
make docker-start-jupyter 2>&1 | tee jupyter.out &

sleep 15

if ! grep -q 'Jupyter Notebook .* is running at' jupyter.out ; then
    echo "Jupyter notebook did not appear to start correctly"
    kill %1
    exit 1
fi

kill %1

make docker-start-api &

sleep 5

if [[ $(curl -X 'POST' \
     "http://localhost:8000/${PROJECT_NAME}/v0.0.1/process-file" \
     -H 'accept: application/json' \
     -H 'Content-Type: multipart/form-data' \
     -F 'files=@Makefile' \
     -F 'some_parameter=something' | grep 'Makefile:application/octet-stream') == "" ]]; then
    echo "Did not get expected output from API"
    kill %1
    exit 1
fi




