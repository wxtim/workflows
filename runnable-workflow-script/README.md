# Simulate branching workflows

Sometimes we want to try out branching workflows to see how the workflow
will handle different pathways. We can use simulation mode to see which
pathways through a workflow are handled.

This toy example has a data gathering task which may sometimes fail. If it
does we want to ignore it and move on.

Run this workflow with:

cylc vip --mode simulation
---
Written for Cylc Version: 8.x
Tested with Cylc Version: 8.3
