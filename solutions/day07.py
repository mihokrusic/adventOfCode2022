def part1(input):
    structure = __get_structure(input)
    return 0

def part2(input):
    return 0

def __get_structure(input):
    input = filter(lambda x: x.rstrip() != '$ ls' and  x.rstrip() != '$ cd /', input)

    print('')
    print('')
    print('')
    for line in input:
        print(line.rstrip())
