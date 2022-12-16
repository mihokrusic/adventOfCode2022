POINTS = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

I_WIN = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

DRAW = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

I_LOSE = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

def part1(input):
    score = 0
    for line in input:
        him, me = line.rstrip().split(' ')
        score += POINTS[me]

        if (I_WIN[him] == me):
            score += 6
        elif DRAW[him] == me:
            score += 3

    return score

def part2(input):
    score = 0
    for line in input:
        him, outcome = line.rstrip().split(' ')
        if outcome == 'X':
            me = I_LOSE[him]
        elif outcome == 'Y':
            me = DRAW[him]
            score += 3
        elif outcome == 'Z':
            me = I_WIN[him]
            score += 6
        score += POINTS[me]

    return score
