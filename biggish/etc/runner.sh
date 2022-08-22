#!/bin/bash

python3 etc/maker.py || exit 1

echo "Made a new workflow!"

# UUID=$(uuidgen)
# NAME="large-demo-${UUID::8}"
EX=$(cat etc/words | shuf -n1)
NAME="large-demo-${EX}"


cylc validate .
cylc install --workflow-name "${NAME}"
cylc play "${NAME}"
