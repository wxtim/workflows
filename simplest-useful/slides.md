# The Simplest Useful Cylc Workflow

## Aim

Show you how to replace a very simple script with a very simple workflow
and get some (nearly) free:

* Error handling
* Efficiency

## The problem...

> I want to get some data...

* 🕰️ Time
* 💔 Reliability

> ... and do some analysis

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

## The Workflow

## graph

```
[scheduling]
    [[graph]]
        R1 = get_data => process_data
```

## get_data

```
[runtime]
    [[get_data]]
        script = get_data.sh
        platform = any_old_server
```

## process_data
```
[runtime]
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

```diff
[[process_data]]
+     execution time limit = PT5M
    [[[directives]]]
-         --time 300   # DONT!
```

**Cylc will know the task has timed out**
**even without communication with the platform!**

## Retries

```diff
[[get_data]]
    script = get_data.sh
    platform = any_old_server
+     execution retry delays = 4*PT15M, PT1D
```

## Aim

Show you how to replace a very simple script with a very simple workflow
and get some (nearly) free:

* Error handling
* Efficiency
