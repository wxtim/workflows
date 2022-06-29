# Remove Cylc Lib from Path
    Help a customer with error from importing jinja2.asyncsupport because
    this was not the version of jinja2 available in the path with the
    CYLC_DIR/lib included.

    Two possible approaches shown:
    - Remove in pre-script: Feels more Cylc style.
    - Remove in Python: Feels horrid. Don
