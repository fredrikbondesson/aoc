from typing import DefaultDict
import util


INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def parse_and_get_from_to_positions(input):
    xy_xy = input.split(' -> ')
    x1, y1 = xy_xy[0].split(',')
    x2, y2 = xy_xy[1].split(',')

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    return (x1, y1), (x2, y2)

def get_nr_of_overlapping_points(input, consider_all=False):
    diagram = DefaultDict(int)

    for row in input:
        (x1, y1), (x2, y2) = parse_and_get_from_to_positions(row)

        stepx = 1 if x1 < x2 else -1
        stepy = 1 if y1 < y2 else -1
        xrange = range(x1, x2 + 1 * stepx, stepx)
        yrange = range(y1, y2 + 1 * stepy, stepy)

        if x1 == x2:
            for ypos in yrange:
                diagram[x1, ypos] += 1
        elif y1 == y2:
            for xpos in xrange:
                diagram[xpos, y1] += 1
        elif consider_all:
            for idx in range(0, len(xrange)):
                diagram[xrange[idx], yrange[idx]] += 1

    length = len([aa for aa in diagram.values() if aa>1])
    return length

    
def main():
    print('Part1: Consider only horizontal and vertical lines.')
    
    length = get_nr_of_overlapping_points(INPUT.split('\n'))
    print(length)
    assert length == 5

    data = util.read_data('2021/day5.txt')
    length = get_nr_of_overlapping_points(data)
    print(length)
    assert length == 6841
   
    print('Part2: Considering all lines')

    length = get_nr_of_overlapping_points(INPUT.split('\n'), consider_all=True)
    print(length)
    assert length == 12

    length = get_nr_of_overlapping_points(data, consider_all=True)
    print(length)
    assert length == 19258


if __name__ == '__main__':
    main()
