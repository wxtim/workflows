from pathlib import Path
import os
import re


JOB_STATUS = re.compile(r'CYLC_JOB_EXIT=(.*)')


def main(tasks, debug=False):
    logdir = Path(os.getenv('CYLC_TASK_LOG_DIR'))
    cycle_log_root = logdir.parent.parent

    if debug: print(tasks)

    task, status = ['Task', 'Status']
    print(f'┌{"─" * 17}┬{"─" * 14}┐')
    print(f'│ {task:15} │ {status:12} │')
    print(f'├{"─" * 17}┼{"─" * 14}┤')

    for task in tasks:
        status_text = (cycle_log_root / 'a/NN/job.status').read_text()
        status = JOB_STATUS.findall(status_text)
        if debug: print(f'{task=}\n{status_text}\n{status=}')
        
        if len(status) == 1:
            status = status[0]
        else:
            status = 'Not Run'
        print(f'│ {task:15} │ {status:12} │')
    print(f'└{"─" * 17}┴{"─" * 14}┘')


if __name__ == "__main__":
    main()

