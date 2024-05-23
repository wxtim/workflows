# Remove Cylc Lib from Path

Help a customer with error from importing jinja2.asyncsupport because
this was not the version of jinja2 available in the path with the
CYLC_DIR/lib included.

Two possible approaches shown:
- Remove in pre-script: Feels more Cylc style.
- Remove in Python: Feels horrid. Don't do this routinely.
---
Written for Cylc Version: 7.8.7
Tested with Cylc Version: 8.1.0
