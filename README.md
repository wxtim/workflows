
# Tim's simple Cylc Examples

A small collection of simple suites.
You may find these easier to start with than writing a suite from scratch.

## Crontab Replacement

* Demonstrates clock triggers.
* Demonstrates replacing Cron.

## Custom memory over time

* Uses Cylc Broadcast to change resource settings for a task on a per-cycle-
  point basis.
* Has a script to find out what Slurm resources Cylc Uses.

## Data Retrieve First

* Demo a very simple pattern where we ensure data has been collected
  before analysing it.

## Five Day Collector

* Collect data for a period, then analyse it.

## Meta Workflow

* Demonstrates how `cylc play -t` can allow you to store separate flows in
  one workflow.