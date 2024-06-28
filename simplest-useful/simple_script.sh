#!/bin/bash
#@supercomputer --time 300
#@supercomputer --memory LOTS
#@supercomputer --CPU MANY

./bin/get_data.sh

./bin/process_data.sh
