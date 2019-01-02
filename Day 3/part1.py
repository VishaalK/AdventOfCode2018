from sys import stdin
import re

my_regex = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')
grid = [[0]*1000 for i in range(1000)]

# instead of removing claims, we can invalidate claims


def read_input():
    valid_claims = set()
    for line in stdin:
        matches = my_regex.match(line)
        id, distanceFromLeft, distanceFromTop, width, height = int(matches[
            1]), int(matches[2]), int(matches[3]), int(matches[4]), int(matches[5])

        for i in range(width):
            for j in range(height):
                grid[distanceFromLeft+i][distanceFromTop+j] += 1


def answer(cells):
    count = 0
    for (i, row) in enumerate(cells):
        for (j, value) in enumerate(row):
            if value >= 2:
                count += 1

    return count


# print(answer(cells))
# print(answer(grid))

def printGrid(grid):
    for row in grid:
        print(''.join([str(val) for val in row]))


def hello():
    read_input()
    print(answer(grid))
    printGrid(grid)


if __name__ == "__main__":
    hello()
