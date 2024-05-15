#!/bin/bash

echo "#" $(cylc config "${1}" -i [meta]title 2> /dev/null )

echo ''

cylc config "${1}" -i [meta]description 2> /dev/null
