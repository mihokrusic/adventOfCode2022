import math

def part1(input):
    priority = 0
    for line in input:
        parsed = line.rstrip()
        left = parsed[:math.trunc(len(parsed) / 2)]
        right = parsed[math.trunc(len(parsed) / 2):]

        left = set(list(left))
        right = set(list(right))
        intersection = left.intersection(right)
        for e in intersection:
            priority += __calc_priority(e)

    return priority

def part2(input):
    priority = 0
    for count, _ in enumerate(input):
        if (count + 1) % 3 != 0:
            continue

        first = set(list(input[count - 2].rstrip()))
        second = set(list(input[count - 1].rstrip()))
        third = set(list(input[count].rstrip()))
        intersection = first.intersection(second).intersection(third)
        for e in intersection:
            priority += __calc_priority(e)

    return priority

def __calc_priority(c):
    if 65 <= ord(c) <= 90:
        return ord(c) - 38
    elif 97 <= ord(c) <= 122:
        return ord(c) - 96
    return 0
