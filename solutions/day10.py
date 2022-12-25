def part1(input):
    x = 1
    cycle = 0
    signal_strength = 0
    check_signals = [[20, False], [60, False], [100, False], [140, False], [180, False], [220, False]]
    for line in input:
        command_arr = line.rstrip().split(' ')
        x_to_add = 0
        if command_arr[0] == 'noop':
            cycle += 1
        elif command_arr[0] == 'addx':
            cycle += 2
            x_to_add = int(command_arr[1])

        for i, [target_cycle, reached] in enumerate(check_signals):
            if not reached and cycle >= target_cycle:
                check_signals[i][1] = True
                signal_strength += (target_cycle * x)

        x += x_to_add

    return signal_strength

def part2(input):
    x = 1
    cycle = 0
    display = []
    print('')
    print('')
    print('')
    for _, line in enumerate(input):
        command_arr = line.rstrip().split(' ')
        x_to_add = 0
        cycles_to_add = 0
        if command_arr[0] == 'noop':
            cycles_to_add = 1
        elif command_arr[0] == 'addx':
            cycles_to_add = 2
            x_to_add = int(command_arr[1])

        for c in range(cycles_to_add):
            col = (cycle + c) % 40
            if col == 0:
                display.append([])

            pixel = '#' if x - 1 <= col <= x + 1 else '.'
            display[len(display) - 1].append(pixel)
        cycle += cycles_to_add
        x += x_to_add

    print('')
    for row in display:
        print(''.join(row))
    print('')

    return 0
