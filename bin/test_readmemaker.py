"""
Tests for the readmemaker scripts.
"""

import sys
import pytest
from pathlib import Path

from .readmemaker import get_title


@pytest.mark.parametrize(
    'testdata, expect',
    [
        (
            """
                [meta]
                    title = Hellooo
            """,
            'Hellooo'
        ),
        (
            """
            """,
            ''
        )
    ]
)
def test_get_title(testdata, expect, capsys):
    assert get_title(testdata, Path.cwd()) == expect
    if expect == '':
        assert "did not find title" in capsys.readouterr().out
