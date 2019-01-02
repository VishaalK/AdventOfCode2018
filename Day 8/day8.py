import re
from collections import namedtuple, deque

# part 1
input = open("day8.txt").readlines()
ints = list(map(int, re.findall('\d+', input[0])))
# print(sum(ints))

ints = deque(ints)

node = namedtuple('node', 'children metadata')

def read_node(ints):
    num_children, ints = ints.popleft(), ints
    num_metadata, ints = ints.popleft(), ints

    children = []
    for i in range(num_children):
        (child, ints) = read_node(ints)
        children.append(child)

    metadata = []
    for i in range(num_metadata):
        metadata.append(ints.popleft())

    n = node(children, metadata)
    return (n, ints)

def sum_of_metadata_nodes(node):
    sumSoFar = sum(node.metadata)

    for child in node.children:
        sumSoFar += sum_of_metadata_nodes(child)

    return sumSoFar

def part_2_sum(node):
    # print('len(node.children:)', len(node.children))
    if len(node.children) == 0:
        # print('no children:', sum(node.metadata))
        return sum(node.metadata)

    # print(node.children)
    sumSoFar = 0
    # print(node.metadata)
    for entry in node.metadata:
        # print('entry: ', entry)
        if (entry <= len(node.children) and entry != 0):
            sumSoFar += part_2_sum(node.children[entry-1])

    # print('end:', sumSoFar)
    return sumSoFar


(tree, _) = read_node(ints)
# print(sum_of_metadata_nodes(tree))
print(part_2_sum(tree))
