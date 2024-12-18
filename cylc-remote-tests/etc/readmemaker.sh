#!/bin/bash
# Create the readmefile

cylc config . -i '[meta]title' > README.md
echo "" >> README.md
cylc config . -i '[meta]description' >> README.md