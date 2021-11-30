import util


def is_outside_grid(row_nr_to_look_in, col_nr_to_look_in):
    return row_nr_to_look_in < 0 or col_nr_to_look_in < 0


def get_from_direction(row_nr, col_nr, row_dir, col_dir, input):
    try:
        row_nr_to_look_in = row_nr + row_dir
        col_nr_to_look_in = col_nr + col_dir
        if is_outside_grid(row_nr_to_look_in, col_nr_to_look_in):
            return ''
        value = input[row_nr_to_look_in][col_nr_to_look_in]
        if value == '.':
            return get_from_direction(row_nr_to_look_in, col_nr_to_look_in, row_dir, col_dir, input)
        else:
            return value
    except IndexError:
        return ''

    assert False


def get_upper_left(row_nr, col_nr, input):
    return get_from_direction(row_nr, col_nr, -1, -1, input)


def get_upper(row_nr, col_nr, input):
    return get_from_direction(row_nr, col_nr, -1, 0, input)


def get_upper_right(row_nr, col_nr, input):
    return get_from_direction(row_nr, col_nr, -1, 1, input)


def get_left(row_nr, col_nr, input):
    return get_from_direction(row_nr, col_nr, 0, -1, input)


def get_right(row_nr, col_nr, input):
    return get_from_direction(row_nr, col_nr, 0, 1, input)


def get_lower_left(row_nr, col_nr, input):
    return get_from_direction(row_nr, col_nr, 1, -1, input)


def get_lower(row_nr, col_nr, input):
    return get_from_direction(row_nr, col_nr, 1, 0, input)


def get_lower_right(row_nr, col_nr, input):
    return get_from_direction(row_nr, col_nr, 1, 1, input)


def row_above_is_free(row_nr, col_nr, input):
    if get_upper_left(row_nr, col_nr, input) == '#':
        return False
    if get_upper(row_nr, col_nr, input) == '#':
        return False
    if get_upper_right(row_nr, col_nr, input) == '#':
        return False

    return True


def same_row_is_free(row_nr, col_nr, input):
    if get_left(row_nr, col_nr, input) == '#':
        return False
    if get_right(row_nr, col_nr, input) == '#':
        return False

    return True


def row_below_is_free(row_nr, col_nr, input):
    if get_lower_left(row_nr, col_nr, input) == '#':
        return False
    if get_lower(row_nr, col_nr, input) == '#':
        return False
    if get_lower_right(row_nr, col_nr, input) == '#':
        return False

    return True


def all_adjacent_free(row_nr, col_nr, input):
    if not row_above_is_free(row_nr, col_nr, input):
        return False

    if not same_row_is_free(row_nr, col_nr, input):
        return False

    if not row_below_is_free(row_nr, col_nr, input):
        return False

    return True


def get_nr_of_occupied_adjacent(row_nr, col_nr, input, column_size, row_size):
    counter = 0
    if get_upper_left(row_nr, col_nr, input) == '#':
        counter += 1
    if get_upper(row_nr, col_nr, input) == '#':
        counter += 1
    if get_upper_right(row_nr, col_nr, input) == '#':
        counter += 1

    if get_left(row_nr, col_nr, input) == '#':
        counter += 1
    if get_right(row_nr, col_nr, input) == '#':
        counter += 1

    if get_lower_left(row_nr, col_nr, input) == '#':
        counter += 1
    if get_lower(row_nr, col_nr, input) == '#':
        counter += 1
    if get_lower_right(row_nr, col_nr, input) == '#':
        counter += 1

    return counter


def compute_next_grid(input):
    grid_with_seats = []
    row_size = len(input)
    for row_nr, row in enumerate(input):
        column_size = len(row)
        new_row = []
        for col_nr, item in enumerate(row):
            if item == 'L':
                if all_adjacent_free(row_nr, col_nr, input):
                    new_row.append('#')
                else:
                    new_row.append(item)
            elif item == '#':
                if get_nr_of_occupied_adjacent(row_nr, col_nr, input, column_size, row_size) >= 5:
                    new_row.append('L')
                else:
                    new_row.append(item)
            else:
                new_row.append(item)

        grid_with_seats.append(''.join(new_row))
    # print('\n'.join(grid_with_seats))
    # print('-------------------------------------------')

    return grid_with_seats


def count_nr_of(item, data):
    data_as_string = ''.join(data)
    return data_as_string.count(item)


def run_with(data, expected_occupied_count, expected_counter):
    new_grid = ''
    old_grid = data
    running = True
    counter = 0
    while (running):
        new_grid = compute_next_grid(old_grid)
        counter += 1
        if new_grid == old_grid:
            running = False
        old_grid = new_grid

    print('counter=' + str(counter))
    occupied_seats = count_nr_of('#', new_grid)
    print('occupied_seats=' + str(occupied_seats))
    assert counter == expected_counter
    assert occupied_seats == expected_occupied_count
    # Small data
    # expected = ['#.L#.L#.L#', '#LLLLLL.LL', 'L.L.L..#..', '##L#.#L.L#', 'L.L#.LL.L#', '#.LLLL#.LL', '..#.L.....', 'LLL###LLL#', '#.LLLLL#.L', '#.L#LL#.L#']
    # assert new_grid == expected


INPUT = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


def main():
    data = INPUT.split('\n')
    # util.measure_time_for(run_with(data, 26, 7))
    util.measure_time_for(run_with, data, 26, 7)

    data = util.read_data('11.data')
    # run_with_data(data, 2134, 87)
    util.measure_time_for(run_with, data, 2134, 87)


if __name__ == '__main__':
    main()
