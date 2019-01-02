import re
from collections import defaultdict, namedtuple
from heapq import heappop, heappush

# task = namedtuple('Task', 'time_left ')

input = open("day7test.txt").readlines()
tasks = tuple(map(lambda x: re.findall(' ([A-Z]) ', x), input))

# time taken for a task
# time left for a task
# worker assigned to task
# num_workers
# get_free_worker
# is finished?

struct Task {
    int time_left;
}

def is_finished(task):
    return task['time_left'] = 