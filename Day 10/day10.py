import re
import time
import numpy

input = open("day10.txt").readlines()
values_as_arr = tuple(map(lambda l: re.findall(r'-?\d+', l), input))
values = tuple(map(lambda l: tuple(map(int, l)), values_as_arr))

points = [(l[0], l[1]) for l in values]
vectors = [(l[2], l[3]) for l in values]

xs = [x for (x,y) in points]
ys = [y for (x,y) in points]

x_max, x_min = max(xs), min(xs)
x_range = x_max - x_min + 1

y_max, y_min = max(ys), min(ys)
y_range = y_max - y_min + 1

print(x_range, y_range)
grid = numpy.array([['.']*1 for i in range(1)])

def execute_turn(points, vectors):
    return [(p[0] + v[0], p[1] + v[1]) for p, v in zip(points, vectors)]

# print(x_range, y_range)
def generate_grid(points, grid, x_min, y_min):
    for p in points:
        grid[p[1]-y_min][p[0]-x_min] = '#'

    return grid

def wipe_grid(points, grid):
    for p in points:
        grid[p[1]-y_min][p[0]-x_min] = '.'

    return grid

def compute_spread(points):
    xs = [x for (x,y) in points]
    ys = [y for (x,y) in points]

    x_max, x_min = max(xs), min(xs)
    x_range = x_max - x_min + 1

    y_max, y_min = max(ys), min(ys)
    y_range = y_max - y_min + 1

    return (x_min, x_max, y_min, y_max)

spread_at_start = compute_spread(points)
# print('start: ', spread_at_start)
 
def grid_as_str(grid, points):
    # length_row = len(grid[0])
    # length_col = len(grid[:,0])
    # (local_x_min, local_x_max, local_y_min, local_y_max) = compute_spread(points)
    # print(x_min, x_max, y_min, y_max)
    # left_cols_to_chop = abs(x_min - local_x_min)
    # right_cols_to_chop = abs(x_max - local_x_max) 

    # top_rows_to_chop = abs(y_min - local_y_min)
    # bottom_rows_to_chop = abs(y_max - local_y_max)

    # print('cols:', left_cols_to_chop, right_cols_to_chop)
    # print('rows:', top_rows_to_chop, bottom_rows_to_chop)
    # grid = [row[left_cols_to_chop:len(row)-right_cols_to_chop] for row in grid]
    # grid = grid[top_rows_to_chop:length_col-bottom_rows_to_chop, left_cols_to_chop:length_row-right_cols_to_chop]

    rows_as_str = [''.join(row) for row in grid]
    grid_as_str = '\n'.join(rows_as_str)

    return grid_as_str

def compute_extrema(points):
    xs = [x for (x,y) in points]
    ys = [y for (x,y) in points]

    x_max, x_min = max(xs), min(xs)
    x_range = x_max - x_min + 1

    y_max, y_min = max(ys), min(ys)
    y_range = y_max - y_min + 1

    return (x_range, y_range)

def drive(grid, points, vectors):
    # try:
    # grid = wipe_grid(points, grid)
    points = execute_turn(points, vectors)
    # grid = generate_grid(points, grid)
    # str = grid_as_str(grid, points)
    spread = compute_spread(points)
    # print(spread)
    extrema = compute_extrema(points)
    bounding_box = extrema[0]*extrema[1]
    t = 1
    while (True):
        # wipe the old points
        # print(extrema)
        # new_grid = wipe_grid(points, grid)
        new_points = execute_turn(points, vectors)
        # new_grid = generate_grid(new_points, new_grid)
        # new_str = grid_as_str(new_grid, new_points)
        new_spread = compute_spread(points)

        new_extrema = compute_extrema(new_points)
        new_bounding_box = new_extrema[0]*new_extrema[1]
        # print(new_str)

        # print(bounding_box, new_bounding_box)
        if (new_bounding_box > bounding_box):
            xs = [x for (x,y) in points]
            ys = [y for (x,y) in points]

            x_max, x_min = max(xs), min(xs)
            x_range = x_max - x_min + 1

            y_max, y_min = max(ys), min(ys)
            y_range = y_max - y_min + 1

            print('ranges:', x_range, y_range)
            grid = numpy.array([['.']*y_range for i in range(x_range)])
            # print(x_range, y_range)
            # grid = numpy.array([['.']*y_range for i in range(x_range)])
            print('points')
            print(points)
            # grid = generate_grid(points, grid, x_min, y_min)
            # str = grid_as_str(grid, points)
            print('time:', t)
            # print(str)
            # print(spread)
            break

        # grid = new_grid
        points = new_points
        # str = new_str
        extrema = new_extrema
        spread = new_spread
        bounding_box = new_bounding_box
        t = t + 1
        # time.sleep(.5)

    # except:
        # print(str)

# drive(grid, points, vectors)
# points = execute_turn(points, vectors)
# str = grid_as_str(generate_grid(points, grid))
# print(str)

drive(grid, points, vectors)
# def drive
# get points, and add velocities at each step to get new points