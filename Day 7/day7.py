# plan from the top down
# write tests for each sub component
# then change the input
import re
from collections import defaultdict
from heapq import heappop, heappush

input = open("day7test.txt").readlines()
tasks = tuple(map(lambda x: re.findall(' ([A-Z]) ', x), input))

root = tasks[0][0]
dag = defaultdict(lambda: [])
dependencies = defaultdict(lambda: [])
for task in tasks:
    dag[task[0]] += [task[1]]
    dependencies[task[1]] += [task[0]]

# print(dag)
# print(dependencies)

# assert dag['A'] == ['B', 'D']
# assert dependencies['E'] == ['B', 'D', 'F']

processed = set()

def traverse_dag(dag, processed):
    h = []
    
    def find_next_task(h, dag, processed):
        # print('find_next_task:', h)
        invalid = []
        next = heappop(h)
        nodeDependencies = dependencies[next]

        validNode = set(nodeDependencies).issubset(processed) 
        while (not validNode):
            invalid.append(next)
            next = heappop(h)
            nodeDependencies = dependencies[next]
            validNode = set(nodeDependencies).issubset(processed)

        for node in invalid:
            heappush(h, node)

        return next

    total = ''
    heappush(h, root)
    while (len(h)):
        next = find_next_task(h, dag, processed)
        # print('h after find_next_task', h)

        if (next not in processed):
            total += next

        processed |= {next}
        children = dag[next]

        for child in children:
            if (child not in processed):
                heappush(h, child)

        # print('after processing:', h)

    return total

total = traverse_dag(dag, processed)
print(total)