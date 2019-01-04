import re

input_lines = open("day12test.txt").readlines()

def parse_initial_state(line):
    return re.findall('([#|.]+)', line)[0]

assert parse_initial_state('initial state: #..#.#..##......###...###\n') == '#..#.#..##......###...###'

def parse_coda(coda):
    return re.findall('([#|.]+)', coda)

assert parse_coda('...## => #\n') == ['...##', '#']