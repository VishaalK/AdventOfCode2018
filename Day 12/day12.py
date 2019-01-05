import re
from collections import defaultdict

input_lines = open("day12test.txt").readlines()

def parse_initial_state(line):
    return re.findall('([#|.]+)', line)[0]

initial_state = '#..#.#..##......###...###'
assert parse_initial_state('initial state: #..#.#..##......###...###\n') == initial_state

def parse_coda(coda):
    return re.findall('([#|.]+)', coda)

assert parse_coda('...## => #\n') == ['...##', '#']

def pad_initial_state(initial_state):
    return '..' + initial_state + '..'

def get_neighborhoods(state, length):
    state = pad_initial_state(state)
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

# print(coda_dict)
assert coda_dict['...##'] == '#'
assert coda_dict['.....'] == '.'

def evolve(state, codas):
    mapped = map(lambda n: codas[n], get_neighborhoods(state, length=neighborhood_length))
    tup = tuple(mapped)
    # print(tup)
    return ''.join(tup)

stage1 = evolve(initial_state, coda_dict)
# expected = '#...#....#.....#..#..#..#.........'
# print('initial:', initial_state)

# print('stage1:', stage1, 'expected:', expected)

# print(len(stage1), len(expected), len(initial_state))
# assert stage1 == expected

def drive(num_generations, state, codas):
    for i in range(num_generations):
        state = evolve(state, codas)

    return sum([i for (i,c) in enumerate(state) if c == '#'])

print(drive(20, initial_state, coda_dict))

'.#....##....#####...#######....#.#..##.'
'#.#..#.#..#.#..#..#..#..#'