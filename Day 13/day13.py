import numpy

loop = r"""
/----\
|    |
|    |
\----/
"""

game_grid = r"""
/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/ 
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


string_to_grid(game_grid)

def create_game_grid(input_lines):
    grid_x = max(map(len, input_lines))
    grid_y = len(input_lines)
    return numpy.array([[' ']*grid_x for i in range(grid_y)])

def tick(world_state):
    return world_state

print(create_game_grid(game_grid.split('\n')))