from sys import stdin
import re

my_regex = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')


def claimStringToStruct(claim):
    matches = my_regex.match(claim)
    id, distanceFromLeft, distanceFromTop, width, height = int(matches[
        1]), int(matches[2]), int(matches[3]), int(matches[4]), int(matches[5])

    return {
        'id': id,
        'distanceFromLeft': distanceFromLeft,
        'distanceFromTop': distanceFromTop,
        'width': width,
        'height': height,
    }


f = open("day3.txt").readlines()
rawClaims = [l.rstrip('\n') for l in f]
claims = [claimStringToStruct(rawClaim) for rawClaim in rawClaims]


def convertClaimsToGrid(claims):
    emptyGrid = [[[]]*1000 for i in range(1000)]
    # print(emptyGrid)
    valid_claims = set()
    for (_, claim) in enumerate(claims):
        # print(claim)
        width, height = claim['width'], claim['height']
        distanceFromLeft, distanceFromTop = claim['distanceFromLeft'], claim['distanceFromTop']
        # print(width, height, distanceFromLeft, distanceFromTop)
        claimId = claim['id']
        valid_claims |= {claimId}
        for i in range(width):
            for j in range(height):
                # print(distanceFromLeft+i-1, distanceFromTop+j-1)
                # print([claim['id']])
                # print(emptyGrid[distanceFromLeft+i -
                                # 1][distanceFromTop+j-1])
                # cell = emptyGrid[distanceFromLeft+i-1][distanceFromTop+j - 1]
                # cell.append(claimId)
                emptyGrid[distanceFromLeft+i-1][distanceFromTop+j -
                                                1] = emptyGrid[distanceFromLeft+i-1][distanceFromTop+j-1] + [claimId]
                # cell = cell + [claimId]
                # print(cell)
                if (len(emptyGrid[distanceFromLeft+i-1][distanceFromTop+j-1]) >= 2):
                    # print("Removing claims: " +
                        #   ','.join(
                            #   str(emptyGrid[distanceFromLeft+i-1][distanceFromTop+j-1])))
                    valid_claims -= set(emptyGrid[distanceFromLeft+i-1]
                                        [distanceFromTop+j-1])

    print(valid_claims)
    return emptyGrid


# claimsAsStructs = [my_regex.match(claims) for claims in claims]
grid = convertClaimsToGrid(claims)


def claimsAsString(claims):
    return '[' + ','.join(str(x) for x in claims) + ']'


def printGrid(grid):
    for (_, row) in enumerate(grid):
        rowAsString = [claimsAsString(val) for val in row]
        print(rowAsString)


def claimsGridToStackGrid(grid):
    totalGrid = ""
    for (_, row) in enumerate(grid):
        rowAsString = ""
        for (_, val) in enumerate(row):
            rowAsString += str(len(val))
        totalGrid += rowAsString + '\n'

    return totalGrid


# printGrid(grid)
newGrid = claimsGridToStackGrid(grid)
# print(newGrid)

# if __name__ == "__main__":
#     solve()
