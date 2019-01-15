import numpy
from collections import namedtuple

Cart = namedtuple('Cart','position direction')

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

def populate_game_grid(lines):
    return numpy.array([list(line) for line in lines])

def get_direction(tile):
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

def get_points_from_grid(grid):
    ret = []
    # print(grid.shape)
    rows, cols = grid.shape[0], grid.shape[1]
    for i in range(rows):
        for j in range(cols):
            # print(grid[i,j])
            if grid[i,j] in ['>', '<', 'v', '^']:
                ret += [Cart(position=(i,j), direction=get_direction(grid[i,j]))]
                # print((i,j))

    return ret

def compute_movements(points, grid):
    # assume they are in correct order
    for cart in points:
        new_position = move_cart(cart)

    # we can assume the points go in order
    # raise Exception("Sup")

north, south, east, west = (0, -1), (0, 1), (1, 0), (-1, 0)

def move_cart(cart):
    cart.position += cart.direction
    return cart.position

def get_new_cart_direction(current_direction, tile):
    if tile == '\\':
        if current_direction == east:
            return south
        elif current_direction == south:
            return east
        elif current_direction == north:
            return west
        elif current_direction == west:
            return north
        else:
            raise Exception("Incorrect \\ direction")
        # east -> south
        # south -> east
        # north -> west
        # west -> north
    elif tile == '/': 
        if current_direction == east:
            return north
        elif current_direction == north:
            return east
        elif current_direction == west:
            return south
        elif current_direction == south:
            return west
        else:
            raise Exception("Incorrect / direction")
        # east -> north
        # north -> east
        # west -> south
        # south -> west
    else:
        return current_direction

# depending on where they end up, we change their direction
assert get_new_cart_direction(north, '\\') == west
assert get_new_cart_direction(west, '/') == south

tile_to_direction = {
    '>' : east,
    '<' : west,
    '^' : north,
    'v' : south
}

direction_to_tile = {
    east: '>',
    west: '<',
    north: '^',
    south: 'v'
}

def update_grid():
    raise Exception("Sup")

def tick(world_state):
    return world_state

def print_grid(points, grid):
    cp = numpy.copy(grid)
    for p in points:
        position = p.position
        cp[position[0], position[1]] = direction_to_tile[p.direction]

    return cp

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

# print('lines:', lines)
grid = populate_game_grid(lines)
print('grid:\n', grid)
points = get_points_from_grid(grid)
print('points:\n', points)

pgrid = print_grid(points, grid)
print('pgrid:\n', pgrid)