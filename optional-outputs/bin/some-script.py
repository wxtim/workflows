#!/usr/bin/env python3
"""A script demonstrating using subprocess to send a cylc message.
"""

import os
from random import randint
from shlex import split
from subprocess import run
import sys


CYLC_WORKFLOW_ID = os.environ['CYLC_WORKFLOW_ID']
CYLC_TASK_JOB = os.environ['CYLC_TASK_JOB']


def _cylc_message(msg):
    """Run Cylc message as a subprocess"""
    run(split(
        f'cylc message {CYLC_WORKFLOW_ID}'
        f' {CYLC_TASK_JOB} "{msg}"'
    ))


def main():
    if randint(1, 4) == 4:
        # Ensure that something is sent to job.out so that you
        # can tell things are not entirely OK:
        print('Oh Dear! Some Specific thing went wrong.', file=sys.stderr)
        _cylc_message('not_available')
    else:
        print('All\'s well', file=sys.stdout)


if __name__ == '__main__':
    main()
