#!/bin/bash
for workflow in */flow.cylc; do
    flowdir=$(dirname "${workflow}")
    echo "${fowdir}"
    cylc lint "./${flowdir}"
done