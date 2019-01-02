import re

input = open("day5.txt").read()


def reacts(left, right):
    if (left != right and (left.upper() == right or left.lower() == right)):
        return True

    return False


assert reacts('a', 'A') == True
assert reacts('A', 'a') == True
assert reacts('a', 'a') == False
assert reacts('a', 'b') == False
assert reacts('A', 'A') == False


def removeReactingPair(input):
    stringModified = False
    for i in range(len(input)-1):
        pair = input[i:i+2]
        # print('Before:', input, pair)
        if (reacts(pair[0], pair[1])):
            input = input[:max(0, i)] + input[i+2:]
            # print('After:', input)
            stringModified = True
            break

    return (stringModified, input)


def removeReactingPairs(input):
    pairsLeft = True
    while (pairsLeft):
        # print('start')
        (stringModified, input) = removeReactingPair(input)
        pairsLeft = stringModified

    return input


# inert = removeReactingPairs(input)
# print(len(inert))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = alphabet.upper()


def part2(input):
    a = [len(removeReactingPairs(re.sub(c, '', input, flags=re.I)))
         for c in ['a', 'b']]
    print(a)
    return min(a)


print(part2(input))
