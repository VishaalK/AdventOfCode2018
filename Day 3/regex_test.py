# 1 @ 509,796: 18x15
import re

# my_regex = re.compile(r'#*(\d)\s@\s*(\d),*(\d):\s*(\d)x*(\d)')
my_regex = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')
m = my_regex.match("#1 @ 509,796: 18x15")

print(m.groups())

for a in m.groups():
    print(type(a))
# print(m[1], m[2], m[3], m[4], m[5])
