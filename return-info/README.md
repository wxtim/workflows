### Passing Station Lists
## Scenario

You have a task which retrieves data from a set of observation
points and passes it to a data processing task.

Some of the sensors are broken some of the time, and you want your data
processing task to know which ones are working (or broken, the principle is
the same).

## Methodologies

1. Use Cylc Broadcast - Modify the task environment by broadcasting environ-
   -ment variables - suitable for smaller amounts of data, if for example
   you want to pass on fewer than a dozen or so broken sensor IDs.
2. Use a file in ~/cylc-run/workflow/share/<cycle>/ to store the data. More
   suitable if you want to store lists of many tens or more working sensors.

There is no reason that the get_stations couldn
