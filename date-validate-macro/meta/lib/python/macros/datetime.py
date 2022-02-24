"""
Rose validator macro for "datetime" types.

Designed to be compatible with both Python 2 and 3 so that the Rose 2 macro
command will work, and so will the Rose 1 GUI.

How to use:
    Edit the list of tuples describing `(section, key)` in OPTIONS_TO_CHECK
    global variable. By default I've set up `[env]DATE` as an example.


TODO:
    - Add more sophisticated interaction with ISOdatetime to help users
      understand what they've done wrong with datetime.
    - Once Python2/Rose1 is no longer in use remove lines marked # 23compat
"""
import re
import subprocess

try:   # 23compat
    from metomi.rose.macro import MacroBase
    from metomi.isodatetime.parsers import TimePointParser
    from metomi.isodatetime.exceptions import IsodatetimeError
    PY_3 = True   # 23compat
except ImportError:   # 23compat
    from rose.macro import MacroBase   # 23compat
    from isodatetime.parsers import TimePointParser, ISO8601SyntaxError   # 23compat
    PY_3 = False   # 23compat


# Extend this list to include all items you want to check:
OPTS_TO_CHECK = [
    ("env", "DATE"),
    ("jinja2:suite.rc", "DATE"),                  # Rose 1 style
    ("template variables", "DATE"),               # Rose 2 style
]


class DatetimeChecker(MacroBase):
    """Checks datetime options."""
    error_text = "Not a valid datetime."
    def validate(self, config, meta_config=None):
        """Return a list of errors, if any."""
        for section, option in OPTS_TO_CHECK:
            node = config.get([section, option])
            if node is None or node.is_ignored():
                continue
            if self.is_valid_datetime(node.value):
                continue
            else:
                self.add_report(section, option, node.value, self.error_text)
        return self.reports

    @staticmethod
    def is_valid_datetime(date):
        """Try and see if isodatetime can validate date."""
        exc = IsodatetimeError if PY_3 else ISO8601SyntaxError   # 23compat
        try:
            TimePointParser().parse(date)
        except exc:   # 23compat - should be `except IsodatetimeError:`
            return False
        else:
            return True