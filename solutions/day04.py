def part1(input):
    contained_pairs = 0
    for line in input:
        left, right = line.rstrip().split(',')
        left_p = [int(x) for x in left.split('-')]
        right_p = [int(x) for x in right.split('-')]
        if left_p[0] <= right_p[0] and left_p[1] >= right_p[1]:
            contained_pairs += 1
        elif right_p[0] <= left_p[0] and right_p[1] >= left_p[1]:
            contained_pairs += 1

    return contained_pairs

def part2(input):
    overlapping_pairs = 0
    for line in input:
        left, right = line.rstrip().split(',')
        left_p = [int(x) for x in left.split('-')]
        right_p = [int(x) for x in right.split('-')]

        if left_p[1] >= right_p[0] and left_p[0] <= right_p[1]:
            overlapping_pairs += 1
        elif right_p[1] >= left_p[0] and right_p[0] <= left_p[1]:
            overlapping_pairs += 1

    return overlapping_pairs
