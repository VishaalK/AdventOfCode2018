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

def compute_movements(points, grid):
    first = points[0]
    tile = grid[first[0], first[1]]
    # we can assume the points go in order
    raise Exception("Sup")

def get_direction(tile):
    north, south, east, west = (0, -1), (0, 1), (1, 0), (-1, 0)
    if tile == '>':
        return east
    elif tile == '<':
        return west
    elif tile == '^':
        return north
    elif tile == 'v':
        return south
    else:
        raise Exception("getting direction for non-directional tile")

# carts are position, directions
def move_cart(cart):
    cart.position += get_direction(cart.tile)
    return cart.position

def update_cart(cart, grid):
    (new_x, new_y) = move_cart(cart)
    cart.tile = grid[x, y]
# depending on where they end up, we change their direction

def update_grid():
    raise Exception("Sup")

def tick(world_state):
    return world_state

# returns pairs of points who collided, should technically only be one
# can make it fast by doing binary search, but linear is probably enough
def collision(just_moved_point, points):
    collisions = [(i, p) for (i, p) in enumerate(points) if p == just_moved_point]
    if (len(collisions)):
        return collisions[0]
    else:
        return 

assert collision((1,2), [(1,2), (3,4)]) == (0,(1,2))

# print(create_game_grid(game_grid.split('\n')))

lines = tuple(map(lambda l: l.rstrip('\n'), open("gridtest.txt").readlines()))
print('lines:', lines)
grid = populate_game_grid(lines)
print(grid)
points = get_points_from_grid(grid)

print(points)