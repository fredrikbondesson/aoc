#https://adventofcode.com/2021/day/1
import sys
import util

INPUT = [199,200,208,210,200,207,240,269,260,263]

def get_nr_of_increased_for_part1(input):
    last_item = sys.maxsize
    increased = 0
    for item in input:
        if item > last_item:
            increased +=1
        last_item = item

    return increased


def get_nr_of_increased_for_part2(input):
    last_meas = sys.maxsize
    increased = 0
    startIdx = 0
    endIdx = 0
    # print(len(input))
    while not endIdx > len(input):
        endIdx = startIdx + 3
        meas = sum(input[startIdx:endIdx])

        if meas > last_meas:
            increased += 1

        startIdx = startIdx + 1
        last_meas = meas

    return increased


if __name__ == '__main__':
    print('Part1:')
    increased = get_nr_of_increased_for_part1(INPUT)
    print(f'Nr of increased: {increased}')
    assert increased == 7

    data = util.read_data_as_int('2021/day1.txt')
    increased = get_nr_of_increased_for_part1(data)
    print(f'Nr of increased: {increased}')
    assert increased == 1754

    print('\nPart2:')
    increased = get_nr_of_increased_for_part2(INPUT)
    print(f'Nr of increased: {increased}')
    assert increased == 5

    increased = get_nr_of_increased_for_part2(data)
    print(f'Nr of increased: {increased}')
    assert increased == 1789
