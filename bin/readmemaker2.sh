#!/bin/bash

echo "#" $(cylc config "${1}" -i [meta]title 2> /dev/null )

echo ''

cylc config "${1}" -i [meta]description 2> /dev/null

echo "---"

echo Written for Cylc Version: $(cylc config "${1}" -i "[meta]written for cylc version")
echo Tested with Cylc Version: $(cylc config "${1}" -i "[meta]tested with cylc version")
