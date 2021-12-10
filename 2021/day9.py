import sys
import util

INPUT="""2199943210
3987894921
9856789892
8767896789
9899965678"""


def get_item_from(row_nr, col_nr, data):
    if row_nr<0:
        return sys.maxsize
    if col_nr<0:
        return sys.maxsize
    try:
        return int(data[row_nr][col_nr])
    except IndexError:
        return sys.maxsize

# Note that neighbour is defined here as up, down, left, and right (and not diagonal)
def get_smallest_neighbour(row_nr, col_nr, data):
    smallest = sys.maxsize
    val = get_item_from(row_nr - 1, col_nr, data)
    if val<smallest:
        smallest = val

    val = get_item_from(row_nr, col_nr - 1, data)
    if val<smallest:
        smallest = val

    val = get_item_from(row_nr, col_nr + 1, data)
    if val<smallest:
        smallest = val

    val = get_item_from(row_nr + 1, col_nr, data)
    if val<smallest:
        smallest = val

    return smallest


def check_neighbours(data):
    sum_smallest = 0
    low_points = []
    for row_nr, row in enumerate(data):
        for col_nr, current_value in enumerate(row):
            smallest = get_smallest_neighbour(row_nr, col_nr, data)
            if smallest and current_value < smallest:
                sum_smallest = sum_smallest + current_value + 1
                low_points.append((col_nr, row_nr))

    return sum_smallest, low_points


def check_basin(col_nr, row_nr, data, checked):
    if (col_nr, row_nr) in checked:
        return 0
    checked.append((col_nr, row_nr))
    how_many = 1

    val = get_item_from(row_nr - 1, col_nr, data)
    if val != sys.maxsize and val != 9:
        how_many += check_basin(col_nr, row_nr - 1, data, checked)

    val = get_item_from(row_nr, col_nr - 1, data)
    if val != sys.maxsize and val != 9:
        how_many += check_basin(col_nr - 1, row_nr, data, checked)

    val = get_item_from(row_nr, col_nr + 1, data)
    if val != sys.maxsize and val != 9:
        how_many += check_basin(col_nr + 1, row_nr, data, checked)

    val = get_item_from(row_nr + 1, col_nr, data)
    if val != sys.maxsize and val != 9:
        how_many += check_basin(col_nr, row_nr + 1, data, checked)

    return how_many


def get_all_basins(low_points, data):
    basins = []
    for col_nr, row_nr in low_points:
        checked = []
        how_many = check_basin(col_nr, row_nr, data, checked)
        basins.append(how_many)

    return basins


def run():
    data = INPUT.split('\n')

    rows = []
    for row in data:
        buf = []
        for nr in row:
            buf.append(int(nr))

        rows.append(buf)

    sum_low_points, low_points = check_neighbours(rows)
    print(sum_low_points)
    assert sum_low_points == 15
    print(low_points)

    all_basins = get_all_basins(low_points, data)

    print(sorted(all_basins)[-3:])
    assert sorted(all_basins)[-3:] == [9, 9, 14]
    assert 9 * 9 * 14 == 1134

    data = util.read_data('2021/day9.txt')
    rows = []
    for row in data:
        buf = []
        for nr in row:
            buf.append(int(nr))

        rows.append(buf)

    sum_low_points, low_points = check_neighbours(rows)
    print(sum_low_points)
    assert sum_low_points == 502

    all_basins = get_all_basins(low_points, data)
    print(sorted(all_basins))
    print(sorted(all_basins)[-3:])
    assert sorted(all_basins)[-3:] == [108, 110, 112]
    assert 108 * 110 * 112 == 1330560


def main():
    run()


if __name__ == '__main__':
    main()
