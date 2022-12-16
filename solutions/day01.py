def part1(input):
    calories = __get_calories(input)
    return calories[0]

def part2(input):
    calories = __get_calories(input)
    return calories[0] + calories[1] + calories[2]

def __get_calories(input):
    calories = []
    current_calories = 0
    for line in input:
        parsed_line = line.rstrip()
        if (len(parsed_line) == 0):
            calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(parsed_line)


    calories.append(current_calories)
    calories.sort(reverse=True)
    return calories

