from pathlib import Path
import random
from itertools import combinations

thisfile = Path(__file__)

for f in thisfile.parent.glob('*.flow'):
    f.unlink()

TASK_SCRIPTS = [
    'sleep {time}'
]
TASK_PLATFORMS = [
    'localhost',
    'spice',
    'spice-dirty',
    'mymachine',
    'hpc1',
    'hpc2',
    'hpc2A-bg'
]


PRIMES = [5, 7, 13, 17, 23, 31]
TASKNAMES = [
    'foo', 'bar', 'baz', 'qux', 'tapir', 'manatee', 'knight', 'bishop', 'rook',
    'crate', 'giraffe', 'enterprise', 'angiosperm', 'ocolot', 'sedam',
    'parsley', 'hummus', 'pomegranite', 'spider'
]


# Generate an interestingly complex graph
for i in [f'PT{x}H' for x in PRIMES]:
    #random.shuffle(TASKNAMES)
    graph = ''
    graph2 = '\n'
    for item in TASKNAMES:
        if random.choice([True, False]) is True:
            if len(graph) == 0:
                graph += f'{item} '
            else:
                graph += f'=> {item}'
            if random.choice([True, False, False, False]) is True:
                graph2 += f'{item}[-PT{random.choice(PRIMES)}H] => {item}\n'
    if graph2 == '\n':
        graph2 += (
            f'{random.choice(TASKNAMES)}[-PT{random.choice(PRIMES)}H] => '
            f'{random.choice(TASKNAMES)}\n'
        )
    graph += (
        f'\n{random.choice(["ADDAMS"])}:succeed-all =>'
        f'{random.choice(["FLINTSTONE", "ROBINSON"])}\n'
    )

    (thisfile.parent / f'{i}.flow').write_text(graph + graph2)


# Generate TASK scripts and hosts.
taskdefs = '[runtime]\n[[ADDAMS]]\n[[FLINTSTONE]]\n[[ROBINSON]]\n'
for i, task in enumerate(TASKNAMES):
    taskdefs += f'    [[{task}]]\n'
    script = random.choice(TASK_SCRIPTS)
    script = script.format(time=random.randint(5, 25))
    taskdefs += f'        script = {script}\n'
    taskdefs += f'        platform = {random.choice(TASK_PLATFORMS)}\n'
    if i < 5:
        taskdefs += (
            '        inherit = '
            f'{random.choice(["ADDAMS"])}\n'
        )
    else:
        taskdefs += (
            '        inherit = '
            f'{random.choice(["FLINTSTONE", "ROBINSON"])}\n'
        )
    taskdefs += '\n'

(thisfile.parent / 'runtime.cylc').write_text(taskdefs)
