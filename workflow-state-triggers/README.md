# Inter-cycling triggering

A demo of using `cylc workflow-state` in other workflows.

This workflow doesn't do much because it's there for the others
to trigger off from:

# xtrigger

The most up-to-date way of doing inter-workflow triggering
using the provided workflow_state xtrigger.

---

# old notation

classic offset notation.

Included in example for reference only - in general
you should prefer xtriggers.

---

# CLI script

Use the CLI ``cylc workflow-state`` command to poll
for the state of the "first" workflow.

---

Written for Cylc Version: 8
Tested with Cylc Version: 8.3.0.dev
