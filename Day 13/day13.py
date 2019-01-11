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


# string_to_grid(game_grid)

def create_game_grid(input_lines):
    grid_x = max(map(len, input_lines))
    grid_y = len(input_lines)
    return numpy.array([[' ']*grid_x for i in range(grid_y)])

def populate_game_grid(lines):
    return numpy.array([list(line) for line in lines])

def get_points_from_grid(grid):
    ret = []
    # print(grid.shape)
    rows, cols = grid.shape[0], grid.shape[1]
    for i in range(rows):
        for j in range(cols):
            # print(grid[i,j])
            if grid[i,j] in ['>', '<', 'v', '^']:
                ret += [(i,j)]
                # print((i,j))

    return ret

def compute_movements():
    raise Exception("Sup")

def update_grid():
    raise Exception("Sup")

def tick(world_state):
    return world_state

# print(create_game_grid(game_grid.split('\n')))

lines = tuple(map(lambda l: l.rstrip('\n'), open("gridtest.txt").readlines()))
print('lines:', lines)
grid = populate_game_grid(lines)
print(grid)
points = get_points_from_grid(grid)

print(points)