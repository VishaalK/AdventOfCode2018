# plan from the top down
# write tests for each sub component
# then change the input
import re
from collections import defaultdict
from heapq import heappop, heappush

input = open("day7.txt").readlines()
tasks = tuple(map(lambda x: re.findall(' ([A-Z]) ', x), input))

dag = defaultdict(lambda: [])
dependencies = defaultdict(lambda: [])
for task in tasks:
    dag[task[0]] += [task[1]]
    dag[task[1]]

    dependencies[task[0]]
    dependencies[task[1]] += [task[0]]

# print(dag)
# print(dependencies)

# the accessible tasks
# the completed tasks
accessible_tasks = set()
completed_tasks = set()

def valid(taskId, completed_tasks):
    # print('deps:', dependencies[taskId])
    return set(dependencies[taskId]).issubset(completed_tasks)

rootTasks = [kv[0] for kv in dependencies.items() if len(kv[1]) == 0]
for task in rootTasks:
    accessible_tasks.add(task)

def select_task(accessible_tasks, completed_tasks):
    validTasks = [taskId for taskId in accessible_tasks if valid(taskId, completed_tasks)]
    return min(validTasks)

total = ''
while (len(accessible_tasks)):
    selected_task = select_task(accessible_tasks, completed_tasks)
    # print(selected_task)
    completed_tasks |= {selected_task}
    total += selected_task

    accessible_tasks -= {selected_task}
    # print(accessible_tasks)

    children = dag[selected_task]
    for child in children:
        if child not in completed_tasks and child not in accessible_tasks:
            accessible_tasks.add(child)

    # print(accessible_tasks)

print(total)