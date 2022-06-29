# Cylc 8 Example Workflow

A workflow designed to do a few stange things for you to look at with Cylc GUI and Tui.

## How to use?

Grab a copy:

```bash
git clone --branch demo --single-branch git@github.com:oliver-sanders/cylc-8-workshops.git

# The rest of this tutorial we assume that you are in the folder you've just created:
cd cylc-8-workshops/gui-demo

# Install the workflow and set it running
cylc install
```

## Things to try:

### Open the workflow Tui or GUI

```bash
cylc tui gui-demo

# or

cylc gui
```

If you opened the GUI, navigate to the workflow.

### Set the workflow running.

Use the play button or the burger bar menu to play the workflow.

For bonus points, consider using the pencil icon and changing some settings:
You could start the workflow paused using the toggle then play it from the main menu.

### Examine individual tasks

Open up tasks to thier maximum extent. Have a look at the jobs submitted by
those tasks.

### Intervene in job submission

One of the tasks is designed to fail on the first job submission (and
randomly on the second). Can you trigger this task from the GUI/Tui?
