import sys
import util

INPUT_SMALL="""
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

INPUT_LARGE="""
..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#
"""
# Part 1
# In this example, traversing the map using this slope would cause you to encounter 7 trees.
# Starting at the top-left corner of your map and following a slope of right 3 and down 1,
# how many trees would you encounter?

# Part 2
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
#
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; 
# multiplied together, these produce the answer 336.

def traverse_playgound(playground, traverse_x=3, traverse_y=1, log=False):
    posX = 0
    posY = 0

    max_x = len(playground[0])
    done = False
    if log:
        print('max_x=' + str(max_x))

    tree_counter = 0
    while not done:
        posX += traverse_x
        posY += traverse_y
        if posX >= max_x:
            posX = posX - max_x
        if log:
            print(posX, posY)
        if posY < len(playground):
            item = playground[posY][posX]
            if item == '#':
                tree_counter += 1
            if log:
                print(posX, posY, item)
        else:
            done = True

    return tree_counter


def main(*_argv):
    playground = INPUT_SMALL.split()
    tree_counter = traverse_playgound(playground)
    assert tree_counter == 7

    playground = INPUT_LARGE.split()
    tree_counter = traverse_playgound(playground)
    assert tree_counter == 7

    playground = util.read_data('3.data')
    tree_counter = traverse_playgound(playground, traverse_x=3, traverse_y=1)
    assert tree_counter == 169

    tree_counter1 = traverse_playgound(playground, traverse_x=1, traverse_y=1)
    assert tree_counter1 == 87

    tree_counter2 = traverse_playgound(playground, traverse_x=3, traverse_y=1)
    assert tree_counter2 == 169

    tree_counter3 = traverse_playgound(playground, traverse_x=5, traverse_y=1)
    assert tree_counter3 == 99

    tree_counter4 = traverse_playgound(playground, traverse_x=7, traverse_y=1)
    assert tree_counter4 == 98

    tree_counter5 = traverse_playgound(playground, traverse_x=1, traverse_y=2)
    assert tree_counter5 == 53

    assert tree_counter1 * tree_counter2 * tree_counter3 * tree_counter4 * tree_counter5 == 7560370818


if __name__ == '__main__':
    print("args=%s" %(sys.argv))
    main(sys.argv)
