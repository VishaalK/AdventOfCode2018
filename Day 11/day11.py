import numpy

def get_hundredths_digit(number):
    return number % 1000 // 10 // 10

assert get_hundredths_digit(12345) == 3
assert get_hundredths_digit(45) == 0

def calculate_power_level(grid_serial_number, x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level = power_level + grid_serial_number
    power_level = power_level * rack_id
    power_level = get_hundredths_digit(power_level)
    power_level = power_level - 5
    return power_level

# Fuel cell at  122,79, grid serial number 57: power level -5.
# Fuel cell at 217,196, grid serial number 39: power level  0.
# Fuel cell at 101,153, grid serial number 71: power level  4.
assert calculate_power_level(57, 122, 79) == -5
assert calculate_power_level(39, 217, 196) == 0
assert calculate_power_level(71, 101, 153) == 4

def generate_grid_points(x_max, y_max):
    for x in range(x_max):
        for y in range(y_max):
            yield (x, y)

def compute_cell_power_level(grid, x, y, cell_size):
    return sum(grid[x+i][y+j] for (i,j) in generate_grid_points(cell_size, cell_size))

def get_filled_grid(grid_size, grid_serial_number):
    grid = numpy.array([[-1]*grid_size for i in range(grid_size)])
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i, j] = calculate_power_level(grid_serial_number, i, j)

    return grid

def compute_max_cell(grid, grid_size):
    cell_power_levels = [(x, y, compute_cell_power_level(grid, x, y)) for (x,y) in generate_grid_points(grid_size - 3, grid_size - 3)]
    return max(cell_power_levels, key=lambda x: x[2])

grid_serial_number = 7403
grid_size = 300

def drive(grid_size, grid_serial_number):
    grid = get_filled_grid(grid_size, grid_serial_number)
    max_cell = compute_max_cell(grid, grid_size)
    return max_cell

def test_one():
    serial_number = 18
    return drive(300, serial_number)

def test_two():
    serial_number = 42
    return drive(300, serial_number)

# print(test_one())
# print(test_two())
print(drive(grid_size, grid_serial_number))
