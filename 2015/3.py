from typing import DefaultDict
import util


INPUT = """^>v<"""

"""
For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""

def count_houses_part1(directions: str) -> int:
    x = 0
    y = 0
    houses =  DefaultDict(int)
    houses[(x, y)] = 1
    for direction in directions:
        if direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        elif direction == '<':
            x -= 1
        elif direction == '>':
            x += 1
        
        houses[(x, y)] += 1

    return houses

"""For example:
    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""
def count_houses_part2(directions: str) -> int:
    santa_x = 0
    santa_y = 0
    robot_x = 0
    robot_y = 0    
    houses =  DefaultDict(int)
    houses[(0, 0)] = 2
    santas_turn = True
    for direction in directions:
        #print(direction)
        if santas_turn:
            santa_x, santa_y = get_position(direction, santa_x, santa_y)
            houses[(santa_x, santa_y)] += 1
            santas_turn = False
        else:
            robot_x, robot_y = get_position(direction, robot_x, robot_y)
            houses[(robot_x, robot_y)] += 1
            santas_turn = True
        #print(houses)

    return houses

def get_position(direction: str, x, y):
    if direction == '^':
        y += 1
    elif direction == 'v':
        y -= 1
    elif direction == '<':
        x -= 1
    elif direction == '>':
        x += 1

    return (x, y)


def main() -> None:
    print('Part1:')
    
    res = count_houses_part1("^")
    assert len(res) == 2

    res = count_houses_part1("^>v<")
    assert len(res) == 4

    res = count_houses_part1("^v^v^v^v^v")
    assert len(res) == 2

    data = util.read_data('2015/day3.txt')
    res = count_houses_part1(data[0])
    print(len(res))
    assert len(res) == 2572

    print('Part2:')
    res = count_houses_part2("^")
    assert len(res) == 2

    res = count_houses_part2("^>v<")
    assert len(res) == 3

    res = count_houses_part2("^v^v^v^v^v")
    assert len(res) == 11
    
    res = count_houses_part2(data[0])
    print(len(res))
    assert len(res) == 2631


if __name__ == '__main__':
    main()
    