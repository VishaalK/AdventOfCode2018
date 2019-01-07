loop = r"""
/----\
|    |
|    |
\----/
"""

# print(loop)

def string_to_grid(string):
    for line in loop.split('\n'):
        print(line)

string_to_grid(loop)