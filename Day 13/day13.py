loop = r"""
/----\
|    |
|    |
\----/
"""

# print(loop)

def string_to_grid(string):
    for line in loop.split('\n'):
        print(line)

# in C++
# grid of track types,
# mutates and updates the grid
# check for collision after each tick
# return once finished

# check for collision complexity
# keep track of the cycle of each cart
# keep track of the direction of each cart

string_to_grid(loop)

def tick(world_state):
        return world_state