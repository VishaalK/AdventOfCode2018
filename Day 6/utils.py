#### IMPORTS

import re
from collections import Counter, defaultdict, namedtuple, deque
from itertools   import chain, cycle, product, count as count_from
from functools   import lru_cache

#### CONSTANTS

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = alphabet.upper()
infinity = float('inf')

#### SIMPLE UTILITY FUNCTIONS

cat = ''.join

def ints(start, end, step=1):
    "The integers from start to end, inclusive: range(start, end+1)"
    return range(start, end + 1, step)

def quantify(iterable, pred=bool):
    "Count how many times the predicate is true of an item in iterable."
    return sum(map(pred, iterable))

def multimap(items):
    "Given (key, val) pairs, return {key: [val, ....], ...}."
    result = defaultdict(list)
    for (key, val) in items:
        result[key].append(val)
    return result

def mapt(fn, *args): 
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))

#### FILE INPUT AND PARSING

def Input(day, line_parser=str.strip, file_template='day{}.txt'):
    "For this day's input file, return a tuple of each line parsed by `line_parser`."
    return mapt(line_parser, open(file_template.format(day)))

def integers(text): 
    "A tuple of all integers in a string (ignore other characters)."
    return mapt(int, re.findall(r'-?\d+', text))

input = Input(6, integers)
print(input)