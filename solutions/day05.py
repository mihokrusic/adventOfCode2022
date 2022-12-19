import math

def solve(input, move_one_by_one = True):
    commands, state = __parse(input)

    for amount, source, target in commands:
        to_move = state[source - 1][-amount:]
        if move_one_by_one:
            to_move.reverse()
        state[source - 1] = state[source - 1][:-amount]
        state[target - 1].extend(to_move)

    return ''.join([c[-1] for c in state])

def __parse(input):
    raw_containers = input[:input.index('\n')]
    raw_commands = input[input.index('\n') + 1:]
    container_count = math.floor((len(raw_containers[-1].rstrip()) + 2) / 4)
    state = []

    for _ in range(container_count):
        state.append([])

    for r in range(len(raw_containers) - 2, -1, -1):
        for c in range(container_count):
            container = raw_containers[r][c * 4:(c + 1) * 4 - 1]
            if len(container.rstrip()) != 0:
                state[c].append(container[1])

    commands = []
    for line in raw_commands:
        commands.append([int(x) for x in line.rstrip().replace('move ', '').replace(' from ', '|').replace(' to ', '|').split('|')])

    return commands, state
