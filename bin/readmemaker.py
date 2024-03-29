#!/usr/bin/env python3
"""Tools for auto generation of readme files from Cylc Metadata.
"""

import argparse
from pathlib import Path
import re
from glob import glob
import logging
from subprocess import run
from shlex import split


RE_DESCRIPTION = r"description\s?=\s?[\"']{1,3}\n?(.+?)(?=[\"']{1,3})"
RE_TITLE = r"title\s?=\s?[\"']?(.+?)(?=[\"'\n])"
WRITTEN_FOR = r"written for cylc.*\s=\s(.*)"
TESTED_WITH = r"teste?d? with cylc\sversion?\s?=\s?(.*)"
META_TABLE_TEMPLATE = '| {title:80} | {written_for:12} | {tested_with:12} |\n'
LINK_STUB='https://github.com/wxtim/workflows/tree/cylc-8/{flowname}'
README_STUB = '''
# Tim's simple Cylc Examples

A small collection of simple suites.
You may find these easier to start with than writing a suite from scratch.

# Index

'''

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

# create logger with 'spam_application'
LOG = logging.getLogger("ReadmeMaker")
LOG.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

LOG.addHandler(ch)



def get_title(data, path):
    """Extract a Cylc Meta title using Regexes"""
    try:
        title = list(re.finditer(RE_TITLE, data, re.MULTILINE))[0].groups()[0]
        return title
    except IndexError:
        logging.warning(f'did not find title in {path}')
        return ''


def get_desc(data, title, path):
    try:
        descriptions = list(
            re.finditer(RE_DESCRIPTION, data, re.MULTILINE | re.DOTALL))
        desc = descriptions[0].groups()[0]
    except IndexError:
        desc = f"[N.B.] Suite {title} does not have a description."
        LOG.warning(f'did not find description in {path}')
    desc += '\n'
    return desc


def get_other_meta(data, regex, path=None):
    """Extract some arbitrary regex"""
    try:
        item = list(re.finditer(regex, data))[0].groups()[0]
    except IndexError:
        LOG.warning(f'did not find {regex} in {path}')
        return ''
    else:
        return item


def build_workflow_readme(path):
    """Extract info from Cylc Meta fields to put into the readme.

    Returns metadata to use in master README.md
    """
    # Don't do anything if Readme is to be left alone:
    if (path.parent / '.readmelock').exists():
        return

    # Create blank readme string.
    readme = ''

    with open(path) as fhandle:
        data = fhandle.read()

    # Attempt to extract fields:
    # Title Field:
    title = get_title(data, path)
    readme += f"### {title}\n"

    # Description
    readme += get_desc(data, title, path)

    with open(path.parent / 'README.md', 'w+') as fh:
        fh.write(readme)


    link = LINK_STUB.format(flowname=path.parent.name)
    desc = f'**[🔗]({link})** {title}'

    return {
        'title': desc,
        'written_for': get_other_meta(data, WRITTEN_FOR, path),
        'tested_with': get_other_meta(data, TESTED_WITH, path),
    }


def make_workflow_table(meta):
    """Takes a list of workflow metadatas and tabulates it."""
    table = META_TABLE_TEMPLATE.format(
        title='Name',
        written_for='Written For',
        tested_with='Tested With'
    )
    table += META_TABLE_TEMPLATE.format(
        title='-'*80,
        written_for='-'*12,
        tested_with='-'*12
    )
    for workflow in meta:
        table += META_TABLE_TEMPLATE.format(
            title=workflow['title'],
            written_for=workflow['written_for'],
            tested_with=workflow['tested_with']
        )
    return table


def identify_workflows(path):
    """Find all workflows in path:

    Args:
        path(Path): Path to search.
    """
    yield from path.glob('*/flow.cylc')
    yield from path.glob('*/suite.rc')


def main():
    workflow_metadatas = []
    for workflow in identify_workflows(Path(__file__).parent.parent):
        workflow_metadata = build_workflow_readme(workflow)
        if workflow_metadata:
            workflow_metadatas.append(workflow_metadata)
    workflow_table = make_workflow_table(workflow_metadatas)

    (Path(__file__).parent.parent / 'README.md').write_text(
        README_STUB + workflow_table
    )


if __name__ == "__main__":
    main()
