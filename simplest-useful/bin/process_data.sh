#!/bin/bash

cylc message -- "what is the shortest possible timespan for a pretend hpc job?"
if [[ ! -f output ]]; then
    echo 'ERROR - NO INPUT DATA!'
    exit 1
fi
sleep 14
