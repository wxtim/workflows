"""Filter provides a list of cylc tests for each job runner.

Use thus: `{{ "<job_runner>" | tests }}`
"""

BS_TESTS = """
tests/functional/cylc-poll/06-loadleveler.t
tests/functional/cylc-poll/07-pbs.t
tests/functional/cylc-poll/08-slurm.t
tests/functional/cylc-poll/09-lsf.t
tests/functional/directives/00-loadleveler.t
tests/functional/directives/02-slurm.t
tests/functional/directives/03-pbs.t
tests/functional/execution-time-limit/02-slurm.t
tests/functional/execution-time-limit/03-pbs.t
tests/functional/job-kill/02-loadleveler.t
tests/functional/job-kill/03-slurm.t
tests/functional/job-kill/04-pbs.t
""".strip().split('\n')


def tests(group='slurm'):
    # Tests:
    # Remove /
    # Remove leading tests/functional
    # Remove trailing .t
    # Add the word test because cylc is not an allowed task name start
    sep = ', '
    tests = []
    for test in BS_TESTS:
        if group in test:
            tests.append(test)
    tests = [
        f"test_{t.split('/')[2]}---{t.split('/')[3]}".replace('.t', '')
        for t in tests
    ]

    fin = sep.join(tests)
    return fin
