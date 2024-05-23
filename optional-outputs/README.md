# Optional outputs

Designed to show how optional outputs could support a workflow making choices.
You need to use -s to set PLATFORM_A, PLATFORM_B and PLATFORM_AB when playing
this workflow*.
There are two tasks which act as examples of branching workflows:
which_computer
    Checks which platform to run a task on. This is designed to simulate
    a task which might check for files on two parallel systems and pick
    one for the follow up task.
copy_ancilliary_data
    Returns a message if the data isn't available. Don't recommend replacing
    failure with optional outputs routinely, but if there is a particular
    failure that you want to handle this is how you might do it.
* You may prefer to use -S with cylc install, in which cases your choices will
  be stored in opt/rose-suite-cylc-install.conf
---
Written for Cylc Version: 8.x
Tested with Cylc Version: 8.0.3
