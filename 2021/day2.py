import util

INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

def get_position_part1(input):
    x = 0
    y = 0
    for row in input:
        #print(row)
        command, units = row.split()
        #print(command, units)
        units = int(units)
        if command == 'forward':
            x += units
        #elif command == 'backward':
        #    x -= units
        elif command == 'down':
            y += units
        elif command == 'up':
            y -= units

    return(x, y)


def get_position_part2(input):
    x = 0
    y = 0
    aim = 0
    for row in input:
        command, units = row.split()
        units = int(units)
        if command == 'forward':
            x += units
            y += aim * units
        elif command == 'down':
            aim += units
        elif command == 'up':
            aim -= units


    return(x, y)


# https://adventofcode.com/2021/day/2
if __name__ == '__main__':
    print('Part1:')
    x, y = get_position_part1(INPUT.splitlines())
    assert x * y == 150

    data = util.read_data('2021/day2.txt')
    x, y = get_position_part1(data)
    assert x * y == 1893605

    print('Part2:')
    x, y = get_position_part2(INPUT.splitlines())
    assert x * y == 900

    x, y = get_position_part2(data)
    assert x * y == 2120734350