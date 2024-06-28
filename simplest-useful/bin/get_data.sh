#!/bin/bash

HEAD="[MY SUPERCOMPUTER] "

echo "${HEAD}Waiting for resources"
sleep 7
echo "${HEAD}"

if [[ -f output ]]; then
    rm output
fi

if [[ $((RANDOM % 4)) == 0 ]]; then
    echo "Data Retrieval Succeeded"
    touch output
    exit 0
else
    echo "Data Retrieval Failed"
    exit 1
fi
