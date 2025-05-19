#!/usr/bin/env python
from pathlib import Path
import os


def main():
    cyclepoint = os.getenv('CYLC_TASK_CYCLE_POINT')
    logdir = Path(os.getenv('CYLC_TASK_LOG_DIR'))
    id = os.getenv('CYLC_TASK_ID')
    tasks = {p.name: p for p in logdir.parent.parent.rglob('*')}

    print(tasks)


if __name__ == "__main__":
    main()

