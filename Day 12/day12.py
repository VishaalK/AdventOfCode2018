import re
from collections import defaultdict

input_lines = open("day12test2.txt").readlines()

def parse_initial_state(line):
    return re.findall('([#|.]+)', line)[0]

initial_state = '#..#.#..##......###...###'
assert parse_initial_state('initial state: #..#.#..##......###...###\n') == initial_state

def parse_coda(coda):
    return re.findall('([#|.]+)', coda)

assert parse_coda('...## => #\n') == ['...##', '#']

def pad_state(initial_state):
    return '..' + initial_state + '..'

def get_neighborhoods(state, length):
    state = pad_state(state)
    return [state[i-length:i+length+1] for (i, _) in enumerate(state) if i >= 2 and i < len(state) - 2]

neighborhood_length = 2
neighborhoods = get_neighborhoods(initial_state, length=neighborhood_length)

assert len(get_neighborhoods(initial_state, length=neighborhood_length)) == len(initial_state)
# assert get_neighborhoods(initial_state, length=neighborhood_length)[0] == '..#..'
# assert get_neighborhoods(initial_state, length=neighborhood_length)[24] == '###..'

def get_codas(input_codas):
    parsed_codas = map(parse_coda, input_codas)
    codas = defaultdict(lambda: '.')
    
    for kv in parsed_codas:
        codas[kv[0]] = kv[1]

    return codas
    # return {kv[0]: kv[1] for kv in parsed_coda}

# print(input_lines[2:])
coda_dict = get_codas(input_lines[2:])

expected_stages = ['...#...#....#.....#..#..#..#...........',
                    '...##..##...##....#..#..#..##..........',
                    '..#.#...#..#.#....#..#..#...#..........',
                    '...#.#..#...#.#...#..#..##..##.........',
                    '....#...##...#.#..#..#...#...#.........',
                    '....##.#.#....#...#..##..##..##........',
                    '...#..###.#...##..#...#...#...#........',
                    '...#....##.#.#.#..##..##..##..##.......',
                    '...##..#..#####....#...#...#...#.......',
                    '..#.#..#...#.##....##..##..##..##......',
                    '...#...##...#.#...#.#...#...#...#......',
                    '...##.#.#....#.#...#.#..##..##..##.....',
                    '..#..###.#....#.#...#....#...#...#.....',
                    '..#....##.#....#.#..##...##..##..##....',
                    '..##..#..#.#....#....#..#.#...#...#....',
                    '.#.#..#...#.#...##...#...#.#..##..##...',
                    '..#...##...#.#.#.#...##...#....#...#...',
                    '..##.#.#....#####.#.#.#...##...##..##..',
                    '.#..###.#..#.#.#######.#.#.#..#.#...#..',
                    '.#....##....#####...#######....#.#..##.']

# print(coda_dict)
# assert coda_dict['...##'] == '#'
# assert coda_dict['.....'] == '.'

def evolve(state, center_idx, codas):
    # add the appropriate amount of empty pots to the left and right
    # this means finding the index of the first and last flowered pots, and if they are too close to the ends,
    # padding the appropriate amount and adjusting the center_idx
    flowered_idxs = [idx for (idx, val) in enumerate(state) if val == '#']
    # print(flowered_idxs)
    first_idx, last_idx = flowered_idxs[0], flowered_idxs[len(flowered_idxs) - 1]
    # print('first:', first_idx, 'last:', last_idx, 'len:', len(state))
    if (first_idx < 2):
        state = '.'*(2 - first_idx) + state
        center_idx = center_idx + (2-first_idx)
    if (last_idx > len(state) - 2):
        state = state + (len(state) - last_idx)*'.'

    mapped = map(lambda n: codas[n], get_neighborhoods(state, length=neighborhood_length))
    tup = tuple(mapped)
    # print('stage', i, ''.join(tup))
    return (''.join(tup), center_idx)


# print('initial_state:', initial_state)
def drive_test(num_generations, state, center_idx, codas, expected_stages):
    for i in range(num_generations):
        (state, center_idx) = evolve(state, center_idx, codas)
        # print('stage', i, state, 'expected:', expected_stages[i], 'center_idx', center_idx)
        # assert state in expected_stages[i]

    return sum([(i-center_idx) for (i,c) in enumerate(state) if c == '#'])

# ans = drive_test(20, initial_state, 0, coda_dict, expected_stages)
# print(ans)

# (stage1, center_idx) = evolve(initial_state, 0, coda_dict)
# expected = '...#...#....#.....#..#..#..#...........'

# print('stage1:', stage1, 'expected:', expected)

# assert stage1 in expected

# (stage2, center_idx) = evolve(stage1, center_idx, coda_dict)
# stage2_expected = '...##..##...##....#..#..#..##..........'

# assert stage2 in stage2_expected

# stage20 = initial_state
# center_idx = 0
# for i in range(20):
#     print('stage', i, stage20)
#     (stage20, center_idx) = evolve(stage20, center_idx, coda_dict)

# stage20_expected = '.#....##....#####...#######....#.#..##.'
# print('stage20:', stage20, 'expected:', stage20_expected)

# assert stage20 in stage20_expected

def drive(num_generations, state, center_idx, codas):
    for i in range(num_generations):
        (state, center_idx) = evolve(state, center_idx, codas)
        print('stage', i, state, center_idx)

    return sum([(i-center_idx) for (i,c) in enumerate(state) if c == '#'])

# assert coda_dict['#....'] == '.'
# assert coda_dict['#..##'] == '#'

initial_state = parse_initial_state(input_lines[0])
print(initial_state)
print(drive(20, initial_state, 0, coda_dict))

# '.#....##....#####...#######....#.#..##.'
# '#.#..#.#..#.#..#..#..#..#