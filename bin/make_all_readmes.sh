#!/bin/bash
for workflow in */flow.cylc; do
    flowdir=$(dirname "${workflow}")
    ./bin/readmemaker2.sh "./${flowdir}" > "./${flowdir}/README.md"
done