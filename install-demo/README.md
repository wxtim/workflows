# Cylc 8 Example Workflow

A reasonably simple workflow designed to show you some Cylc 8 features.

## How to use?

Grab a copy:

```bash
git clone --branch demo --single-branch git@github.com:oliver-sanders/cylc-8-workshops.git

# The rest of this tutorial we assume that you are in the folder you've just created:
cd cylc-8-workshops/install-demo
```

## Things to try:

### `cylc validate`

You can validate [Cylc Workflows]()...

```bash
cylc validate .
```

**and** Rose Configurations (including opotional configs!) using:

```bash
cylc validate . --opt-conf-key=one-year
```

**and** the optional configs work with most of the CLI!

```bash
cylc graph . --opt-conf-key=silly
```

(unless they are plain wrong!)

```bash
cylc graph . --opt-conf-key=wrong
```

### `cylc install`

You can install the workflow with the vanilla config or the optional config

```bash
# Do both...
cylc install
cylc install --opt-conf-key=one-year --suite-defines 'TASK_NAME="my_task_"'
```

Then you can have a look at what's been installed:

```bash
tree ~/cylc-run/install-demo/
```

Notice that you have not installed over the top but have run1 and run2 directories:
This is much safer than rose-suite run (use `cylc reinstall` to over-write
what you had before).

Note that you can now find out which rose options were set:
```bash
cat ~/cylc-run/install-demo/run2/rose-suite.conf
```

And which options were set on the command line:
```bash
cat ~/cylc-run/install-demo/run2/opt/rose-suite-cylc-install.conf
```

### `cylc install` II: Rose suite-run strikes back?

You can specify run names and workflow names, or lack of:

```
cylc install --workflow-name "your-workflow-own-name-here1" --no-run-name
cylc install --workflow-name "your-workflow-own-name-here2" --run-name experiment_A
cylc install --workflow-name "your-workflow-own-name-here2" --run-name experiment_B

ls ~/cylc-run/your-workflow-own-name-here/*
```

You can re-install over an existing installed workflow (similar to `rose suite-run`):

```bash
cylc reinstall
cylc reinstall --workflow-name "your-workflow-own-name-here1" --no-run-name
```

### `cylc play`

Replaces cylc run

```bash
cylc play install-demo    # (play runN, the most recent install)
cylc play install-demo/run1
```

look at what you've done:

```
cylc tui install-demo
```

### `cylc clean`

If you've installed this workflow a few times you might want to have a go
at cleaning it up from your run directory:

```bash
cylc clean install-demo/run1

# or all

cylc clean install-demo
```

### Other Commands (`cylc pause`, `cylc stop`, `cylc clean`)

- `cylc pause` prevents the submission of any task jobs.
- `cylc stop` shuts the workflow down.
- `cylc clean` cleans up the run directory.


### Bonus excercise

Try to modify the suite.rc to get rid of the yellow warnings on validate.

To see what changes might be needed:

```bash
diff suite.rc .flow.cylc
```

