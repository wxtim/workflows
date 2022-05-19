#!/usr/bin/env python3
# This script is designed to install and run

from dataclasses import dataclass
from pathlib import Path
from re import findall
from shlex import split
from subprocess import run
from datetime import datetime

WORKFLOWSPATH=Path("/home/h02/tpilling/metomi/workflows/")


@dataclass
class WorkflowInfo:
    """Simple Store of data"""
    name: str
    opt: str
    srcpath: Path


def get_list_of_workflows(folder):
    """Get a list of workflows to be run.
    """
    tstamp = datetime.now().strftime('%Y%m%dT%H%M%S')
    workflows = []
    for flow in folder.glob('*/flow.cylc'):
        workflows.append(WorkflowInfo(
            f'{flow.parent.name}.{tstamp}', None, flow.parent))

    for flow in folder.glob('*/opt/rose-suite-*.conf'):
        optionname = findall('rose-suite-(.*)\.conf', str(flow.name))[0]
        workflows.append(WorkflowInfo(
            name=f'{flow.parent.parent.name}.{optionname}.{tstamp}',
            opt=optionname,
            srcpath=flow.parent.parent
        ))
    return workflows


def copy_workflows(workflows):
    """Copy folder to `~/cylc-src` for further editing."""
    ...


def validate_workflows(workflows):
    for flow in workflows:
        output = run(
            split(
                'cylc validate .'
            ),
        cwd=flow.srcpath,
        capture_output=True
        )
        if output.returncode != 0:
            raise Exception(
                f'ERROR: Validating {flow.name} failed with: {output.stderr}')


def install_workflows(workflows):
    for flow in workflows:
        opt = ''
        if flow.opt:
            opt = f'-O {flow.opt}'
        output = run(
            split(
                'cylc install '
                f'-C {flow.srcpath} '
                f'{opt} '
                f'--flow-name {flow.name}'
            ),
        capture_output=True
        )
        if output.returncode != 0:
            print(
                f'ERROR: Installing {flow.name} failed with: {output.stderr}')
        else:
            print(f'{output.stdout.decode()}')


def run_workflows(workflows):
    for flow in workflows:
        output = run(
            split(
                'cylc play '
                f'{flow.name}'
            ),
        cwd=flow.srcpath,
        capture_output=True
        )
        if output.returncode != 0:
            print(
                f'ERROR: Validating {flow.name} failed with: {output.stderr}')


def main():
    workflows = get_list_of_workflows(WORKFLOWSPATH)
    validate_workflows(workflows)
    install_workflows(workflows)
    run_workflows(workflows)


if __name__ == '__main__':
    main()
