def solve(input, marker_length):
    for x in range(0, len(input.rstrip()) - marker_length + 1, 1):
        unique_cnt = len(set(input[x:x+marker_length]))

        if unique_cnt == marker_length:
            return x + marker_length

    return -1
