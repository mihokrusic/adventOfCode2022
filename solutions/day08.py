import math

def part1(input):
    arr = __get_arr(input)
    visible_cnt = 0
    for y, row in enumerate(arr):
        for x, _ in enumerate(row):
            column = [row[x] for row in arr]
            if y == 0 or y == len(input) - 1 or x == 0 or x == len(row) - 1:
                visible_cnt += 1
                continue

            left = max(row[:x])
            right = max(row[x + 1:])
            top = max(column[:y])
            bottom = max(column[y + 1:])
            all_min = min(left, right, top, bottom)
            if row[x] > all_min:
                visible_cnt += 1

    return visible_cnt

def part2(input):
    arr = __get_arr(input)
    max_scenic_score = 0
    for y, row in enumerate(arr):
        for x, _ in enumerate(row):
            column = [row[x] for row in arr]
            scenic_score = 1 * __get_scenic_index(row, x) * __get_scenic_index(column, y)
            max_scenic_score = max(scenic_score, max_scenic_score)

    return max_scenic_score

def __get_arr(input):
    arr = []
    for y, line in enumerate(input):
        arr.append([])
        for tree in line.rstrip():
            arr[y].append(int(tree))
    return arr

def __get_scenic_index(arr, pos):
    value = arr[pos]
    left = pos
    right = pos
    left_done = False
    right_done = False
    while True:
        if not left_done:
            if (left == 0 or (left != pos and arr[left] >= value)):
                left_done = True
            else:
                left -= 1

        if not right_done:
            if (right == len(arr) - 1 or (right != pos and arr[right] >= value)):
                right_done = True
            else:
                right += 1

        if left_done and right_done:
            break

    return ((pos - left)) * ((right - pos))
