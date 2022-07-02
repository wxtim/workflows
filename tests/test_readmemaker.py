"""
Tests for the readmemaker scripts.
"""

import sys
import pytest

breakpoint()

@pytest.mark.parametrize(
    'testdata, expect',
    [
        (
            """
                [meta]
                    title = Hellooo
            """,
            'Hellooo'
        )
    ]
)
def test_get_title(testdata, expect):
    assert get_title(testdata) == expect