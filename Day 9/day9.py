# don't care about complexity
# do TDD, improve Complexity later
from collections import defaultdict

def clockwise_idx(list, current_marble_idx, steps):
    return (current_marble_idx + steps) % len(list)

assert clockwise_idx([0], 0, 0) == 0
assert clockwise_idx([0,1], 0, 1) == 1
assert clockwise_idx([0,1], 0, 2) == 0
assert clockwise_idx([0,1], 1, 2) == 1
assert clockwise_idx([0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15], 13, -7) == 6

def execute_special_turn(current_list, marble_number_to_insert, current_marble_idx, scores, current_player):
    # print(current_player)
    new_marble_number = marble_number_to_insert + 1
    scores[current_player] += marble_number_to_insert

    seven_to_left_idx = clockwise_idx(current_list, current_marble_idx, -7)
    scores[current_player] += current_list[seven_to_left_idx]
    del current_list[seven_to_left_idx]
    new_current_marble = clockwise_idx(current_list, seven_to_left_idx, 1) - 1

    return (current_list, new_marble_number, new_current_marble, scores)

# returns (new_list, new_current_marble_idx, scores)
def execute_turn(current_list, marble_number_to_insert, current_marble_idx, scores, current_player):
    # if marble_number_to_insert is a multiple of 23, we have to do somehting different
    multiple_of_23 = marble_number_to_insert % 23 == 0
    # print('player:',current_player)
    if multiple_of_23:
        return execute_special_turn(current_list, marble_number_to_insert, current_marble_idx, scores, current_player)

    new_marble_number = marble_number_to_insert + 1
    first_idx = clockwise_idx(current_list, current_marble_idx, 1)
    second_idx = clockwise_idx(current_list, current_marble_idx, 2)
    # print(first_idx, second_idx)
    
    if (second_idx == 0):
        idx = len(current_list)
        current_list.append(marble_number_to_insert)
        return (current_list, new_marble_number, idx, scores)
    else:
        current_list.insert(second_idx, marble_number_to_insert)

    return (current_list, new_marble_number, second_idx, scores)

def run_test(input, expected):
    turn = execute_turn(*input)
    print(turn)
    a,b,c = expected
    assert turn == (a,b,c)

turn1 = execute_turn([0], 1, 0, {}, 0)
# print(turn1)
assert turn1 == ([0,1], 2, 1, {})

turn2 = execute_turn([0,1], 2, 1, {}, 0)
# print(turn2)
assert turn2 == ([0,2,1], 3, 1, {})

turn3 = execute_turn([0,2,1], 3, 1, {}, 0)
# print(turn3)
assert turn3 == ([0, 2, 1, 3], 4, 3, {})

special_turn = execute_special_turn([0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15], 23, 13, defaultdict(lambda: 0), 4)
# print(special_turn)
assert special_turn[0] == [0, 16, 8, 17, 4, 18, 19, 2, 20, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15]
assert special_turn[1] == 24
assert special_turn[2] == 6

def format(i, x, current_marble_idx): 
    return '(' + str(x) + ')' if i == current_marble_idx else str(x)

def list_as_string(list, current_marble_idx):
    return ' '.join([format(i, x, current_marble_idx) for i, x in enumerate(list)])

def drive_game(num_players, highest_value_marble):
    scores = defaultdict(lambda: 0)
    (list, current_marble_number, current_marble_idx) = ([0], 1, 0)
    for i in range(highest_value_marble):
        current_player = (i % num_players)+ 1
        # print('current_player:', current_player)
        (list, current_marble_number, current_marble_idx, scores) = execute_turn(list, current_marble_number, current_marble_idx, scores, current_player)
        # print('[' + str(current_player) + ']', list_as_string(list, current_marble_idx))

    # print(scores)
    return max([v for k, v in scores.items()])

print(9, 25, drive_game(9, 25))
print(10, 1618, drive_game(10, 1618))
print(13, 7999, drive_game(13, 7999))
print(17, 1104, drive_game(17, 1104))
print(21, 6111, drive_game(21, 6111))
print(30, 5807, drive_game(30, 5807))
print(412, 100*71646, drive_game(412, 100*71646))

# 412 players; last marble is worth 71646 points

# 10 players; last marble is worth 1618 points: high score is 8317
# 13 players; last marble is worth 7999 points: high score is 146373
# 17 players; last marble is worth 1104 points: high score is 2764
# 21 players; last marble is worth 6111 points: high score is 54718
# 30 players; last marble is worth 5807 points: high score is 37305
