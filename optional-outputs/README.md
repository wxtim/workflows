### Optional outputs
Designed to show how optional outputs could support a workflow making choices.

You need to use -s to set PLATFORM_A, PLATFORM_B and PLATFORM_AB when playing
this workflow*.

There are two tasks which act as examples of branching workflows:

which_computer
    Checks which platform to run a task on. This is designed to simulate
    a task which might check for files on two parallel systems and pick
    one for the follow up task.

copy_ancilliary_data
    Returns a message if the data isn
