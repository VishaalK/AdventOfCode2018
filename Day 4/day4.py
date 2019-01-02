from datetime import datetime
from dateutil.parser import parse
import re
from collections import defaultdict, namedtuple

lineRegex = re.compile('\\[(.*)\\](.*)')
State = namedtuple('State', 'current_id current_time')


def lineToValues(line):
    line = line.strip()
    matches = lineRegex.match(line)
    return {
        'original': line,
        'timestamp': parse(matches.group(1)),
        'action': matches.group(2).strip()
    }


inputAsLines = open("day4.txt").readlines()
inputs = [lineToValues(line) for line in inputAsLines]
sortedInputs = sorted(inputs, key=lambda p: p['timestamp'])
# filteredInputs = [line['original'] for line in sortedInputs]
# print(sortedInputs)

# now we process things one by one
# have a dictionary of each guard's ID mapped to their time asleep
# at the end, we can retrieve the guard who was asleep the most and the minute they were asleep the most

guards = dict()

guardRegex = re.compile('Guard #(.*) begins shift')

# map<string, array<60, int>> guardsToSleeping
guardsToSleeping = defaultdict(lambda: [0]*60)


def processTimestamp(event, state):
    action = event['action']
    timestamp = event['timestamp']
    if 'Guard' in action:
        s = state._replace(current_id=guardRegex.match(
            action).group(1), current_time=timestamp.minute)
    elif 'falls asleep' in action:
        # they were awake before, so this didn't matter
        s = state._replace(current_time=timestamp.minute)
    else:
        # they woke up, so grab the time they woke up
        # print(current_id)
        # updated = []*(timestamp.minute - state.current_time)
        updated = [a + 1 for a in guardsToSleeping[state.current_id]
                   [state.current_time:timestamp.minute]]
        guardsToSleeping[state.current_id][state.current_time:timestamp.minute] = updated
        s = state._replace(current_time=timestamp.minute)

    return s


def processInputs(sortedInputs):
    s = State(-1, -1)

    for _, x in enumerate(sortedInputs):
        s = processTimestamp(x, s)


def getMostSleepyGuard(guardsToSleeping):
    # for guard, times in guardsToSleeping.items():
    return max(guardsToSleeping.items(), key=lambda kv: sum(kv[1]))


# print(sortedInputs)
# [processTimestamp(a) for a in sortedInputs]

processInputs(sortedInputs)
# print(guardsToSleeping)
mostSleepyGuard = getMostSleepyGuard(guardsToSleeping)
mostSleepyMinutes = mostSleepyGuard[1]
mostSleepyMinute = mostSleepyMinutes.index(max(mostSleepyMinutes))

# print("Most sleepy guard:", mostSleepyGuard)
print("Most sleepy minute:", mostSleepyMinute)
print("Most sleepy id:", mostSleepyGuard[0])

print(int(mostSleepyGuard[0])*int(mostSleepyMinute))


def getMostConsistentlyAsleepGuard(guardsToSleeping):
    return max(guardsToSleeping.items(), key=lambda kv: max(kv[1]))


mostConsistentlyAsleepGuard = getMostConsistentlyAsleepGuard(guardsToSleeping)
mostConsistentlyAsleepMinutes = mostConsistentlyAsleepGuard[1]
mostConsistentlyAsleepMinute = mostConsistentlyAsleepMinutes.index(
    max(mostConsistentlyAsleepMinutes))

print("Guard that was asleep the most minute:", mostConsistentlyAsleepGuard)
print("Minute that was most frequently asleep", mostConsistentlyAsleepMinute)

print(int(mostConsistentlyAsleepGuard[0])*int(mostConsistentlyAsleepMinute))
