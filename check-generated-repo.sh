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
    echo "Run \"rm -rf $ROOT_DIR/pipeline-$PROJECT_NAME\" to clean up the generated pipeline repository.";
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

# Generate a new pipeline repo. 
# Extra whitespace lines in command input to accept defaults after entering Project Name
rm -rf pipeline-$PROJECT_NAME
make generate-repo << EOF
$PROJECT_NAME



EOF

# Change directory to the generated repo and set up the project
cd pipeline-$PROJECT_NAME
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
make pip-compile
make install

# Run required checks
make check
make tidy
make check-notebooks
check_generated_api_diff

# Run tests
make test
