# The Simplest Useful Cylc Workflow

## Aim

Show you how to replace a very simple script with a very simple workflow
and get some (nearly) free:

* Error handling
* Efficiency

## The problem...

> I want to get some data...

Limited by:

* 🕰️ Time (It might take a while)
* 💔 Reliability (You don't control the data source)

> ... and do some analysis

Limited by:

* 🐏 Memory
* 🍟 Processor Power

## The original Script:

```bash
#!/bin/bash
#@supercomputer --time 300
#@supercomputer --memory LOTS
#@supercomputer --CPU MANY

./bin/get_data.sh

./bin/process_data.sh
```

### Problems:

* We've requested supercomputer time (that we don't need)
  for the data retrieval step.
* If the data retrieval step fails then:
  * We've wasted a supercomputer allocation.
  * We're going to have to manually run the whole thing again.


## The Workflow

## graph

```
[scheduling]
    [[graph]]
        R1 = get_data => process_data

[runtime]
    [[get_data]]
        script = get_data.sh
        platform = any_old_server

    [[process_data]]
        script = process_data.sh
        platform = supercomputer
        [[[directives]]]
            --time 300   # DONT!
            --memory LOTS
            --CPU MANY
```

## Gains so far

* 💰 get_data fails => no supercomputer resource request
* 🏃 ``cylc install`` => run dir
* 📕 Cylc's logging facilities

But there's more...

## A Cylc Anti Pattern

**Avoid using batch system time directives**

If you use Cylc's built in ``[runtime][<namespace>]execution time limit``
configureation Cylc will convert this into the appropriate directive,
_and_ Cylc will know that a task have timed out, even if it cannot
contact a remote platform!

```diff
[[process_data]]
+     execution time limit = PT5M
    [[[directives]]]
-         --time 300   # Anti pattern
```

## Retries

**We also get retries on our flaky task with 1 extra line**

```diff
[[get_data]]
    script = get_data.sh
    platform = any_old_server
+     # Retry after 15 minutes 4x then give it another
+     # go tomorrow.
+     execution retry delays = 4*PT15M, PT1D
```

## Very simple parallelization

> [!NOTE]
> This is a response to a question from the talk, from memory:
>
> _How do I run two data processing tasks after my data retrieval?_

### Simple answer

```diff
[scheduling]
    [[graph]]
-         R1 = get_data => process_data
+         R1 = get_data => process_data & process_data2


[runtime]
    [[get_data]]
        script = get_data.sh
        platform = any_old_server

    [[process_data]]
        script = process_data.sh
        platform = supercomputer
        [[[directives]]]
            --time 300   # DONT!
            --memory LOTS
            --CPU MANY

+     [[process_data2]]
+         script = process_data2.sh
+         platform = supercomputer
+         [[[directives]]]
+             --time 300   # DONT!
+             --memory LOTS
+             --CPU MANY

```

### Tidy answer

Abstract the common stuff out of the ``process_data`` tasks.

```diff
[scheduling]
    [[graph]]
-         R1 = get_data => process_data
+         R1 = get_data => process_data & process_data2


[runtime]
    [[get_data]]
        script = get_data.sh
        platform = any_old_server

+     [[PROCESS_DATA]]
-     [[process_data]]
-         script = process_data.sh
        platform = supercomputer
        [[[directives]]]
            --time 300   # DONT!
            --memory LOTS
            --CPU MANY
+
+     [[process_data]]
+         inherit = PROCESS_DATA
+         script = process_data.sh
+
+     [[process_data2]]
+         inherit = PROCESS_DATA
+         script = process_data2.sh

```

> [!TIP]
> If you need less or more resources (memory, CPU, time),
> you can override the defaults from the inheritance in
> individual tasks.
