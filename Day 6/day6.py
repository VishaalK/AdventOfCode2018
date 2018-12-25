import re
import operator
from collections import defaultdict

input = open("day6.txt").readlines()
coordinates = tuple(map(lambda line: tuple(map(int, re.findall('\d+', line))), input))

# print(coordinates)

xMax, yMax = max([x[0] for x in coordinates])+1, max([x[1] for x in coordinates])+1

# make a grid of xMax, yMax
grid = [[0]*yMax for i in range(xMax)]

# once we have placed all the points on the grid
# we want to iterate the entire thing and get the closest one to each point
def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def closest_coordinate(p1, coordinates):
    # If two points are equally close, we don't want any
    minItem = min(enumerate(coordinates), key=lambda item: manhattan(p1, item[1]))
    minDistance = manhattan(p1, minItem[1])

    allMinItems = [item for item in enumerate(coordinates) if manhattan(p1, item[1]) == minDistance]
    
    return minItem[0] if len(allMinItems) == 1 else '.'

def closest_coordinate_p2(p1, coordinates):
    totalDistance = sum([manhattan(p1, coord) for coord in coordinates])
    return '#' if totalDistance < 10000 else '.'

# calculate all the places in the grid 
def calculate_distances(grid, coordinates):
    for i in range(xMax):
        for j in range(yMax):
            # print(i,j)
            grid[i][j] = closest_coordinate((i,j), coordinates)

def calculate_distances_p2(grid, coordinates):
    for i in range(xMax):
        for j in range(yMax):
            # print(i,j)
            grid[i][j] = closest_coordinate_p2((i,j), coordinates)

# calculate_distances(grid, coordinates)

def disqualify_coordinates(grid, coordinates):
    # iterate through edges of the grid
    for i in range(xMax):
        coordinates.discard(grid[i][0])
        coordinates.discard(grid[i][yMax - 1])

    for i in range(yMax):
        coordinates.discard(grid[0][i])
        coordinates.discard(grid[xMax-1][i])

    return coordinates

# coordinate_ids = set(range(len(input)))
# remaining_points = disqualify_coordinates(grid, coordinate_ids)
# remaining_points.discard('.')

def calculate_areas(grid, remaining_points):
    areas = defaultdict(lambda: 0)
    for i in range(xMax):
        for j in range(yMax):
            if (grid[i][j] in remaining_points):
                areas[grid[i][j]] += 1

    return areas

# print(grid)
# areas = calculate_areas(grid, remaining_points)

# we want to disqualify any points that are on the exterior of the grid, since those will go on forever
# which means iterating through the outside of our grid
# print(grid)
# print(areas)
# print(max(areas.items(), key=operator.itemgetter(1))[1])

def calculate_areas_p2(grid):
    size = 0
    for i in range(xMax):
        for j in range(yMax):
            if (grid[i][j] == '#'):
                size += 1
    return size

calculate_distances_p2(grid, coordinates)
ans = calculate_areas_p2(grid)
print(ans)