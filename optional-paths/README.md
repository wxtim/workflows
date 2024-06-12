# Demo optional output funtionality

Advanced use cases for optional outputs:
    1. Graph Branching - Depending upon the output of a task
       the workflow will go down different paths.
    2. Pre-finish triggering - A long running task can emit outputs
       allowing downstream tasks to start sooner.
n.b. Task messages have been elevated to warning to help you
follow events if you choose to run the workflow on the command line.
---
Written for Cylc Version: 8.x
Tested with Cylc Version: 8.3.0.dev (pre-release copy)
