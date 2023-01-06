#!/bin/bash
PROJECT_NAME=testproject
SCRIPT_RELATIVE_DIR=$(dirname "${BASH_SOURCE[0]}") 
cd $SCRIPT_RELATIVE_DIR 
ROOT_DIR=$(pwd)

set -e

handle_error () {
    echo "command \"$BASH_COMMAND\" failed with exit code $?.";
}

cleanup () { 
    echo "Cleaning up..."
    rm -rf $ROOT_DIR/pipeline-$PROJECT_NAME;
}

check_generated_api_diff() {
    mkdir -p pregenerated_prepline_$PROJECT_NAME/api
    mv prepline_$PROJECT_NAME/api/* pregenerated_prepline_$PROJECT_NAME/api/
    make generate-api
    diff -x "__pycache__" prepline_$PROJECT_NAME/api pregenerated_prepline_$PROJECT_NAME/api
    rm -rf pregenerated_prepline_$PROJECT_NAME/api
}

trap 'cleanup' EXIT
trap 'handle_error' ERR

make generate-repo << EOF
$PROJECT_NAME



EOF

cd pipeline-$PROJECT_NAME
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
make install

make check
make tidy
make check-notebooks

check_generated_api_diff

make test

