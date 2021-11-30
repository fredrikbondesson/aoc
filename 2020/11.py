import util


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


def get_upper_left(row_nr, col_nr, input):
    try:
        if row_nr - 1 < 0 or col_nr - 1 < 0:
            return ''
        return input[row_nr - 1][col_nr - 1]
    except IndexError:
        return ''


def get_upper(row_nr, col_nr, input):
    try:
        if row_nr - 1 < 0:
            return ''
        return input[row_nr - 1][col_nr]
    except IndexError:
        return ''


def get_upper_right(row_nr, col_nr, input):
    try:
        if row_nr - 1 < 0:
            return ''
        return input[row_nr - 1][col_nr + 1]
    except IndexError:
        return ''


def get_left(row_nr, col_nr, input):
    try:
        if col_nr - 1 < 0:
            return ''
        return input[row_nr][col_nr - 1]
    except IndexError:
        return ''


def get_right(row_nr, col_nr, input):
    try:
        return input[row_nr][col_nr + 1]
    except IndexError:
        return ''


def get_lower_left(row_nr, col_nr, input):
    try:
        if col_nr - 1 < 0:
            return ''
        return input[row_nr + 1][col_nr - 1]
    except IndexError:
        return ''


def get_lower(row_nr, col_nr, input):
    try:
        return input[row_nr + 1][col_nr]
    except IndexError:
        return ''


def get_lower_right(row_nr, col_nr, input):
    try:
        return input[row_nr + 1][col_nr + 1]
    except IndexError:
        return ''


def all_adjacent_free(row_nr, col_nr, input, column_size, row_size):
    if get_upper_left(row_nr, col_nr, input) == '#':
        return False
    if get_upper(row_nr, col_nr, input) == '#':
        return False
    if get_upper_right(row_nr, col_nr, input) == '#':
        return False

    if get_left(row_nr, col_nr, input) == '#':
        return False
    if get_right(row_nr, col_nr, input) == '#':
        return False

    if get_lower_left(row_nr, col_nr, input) == '#':
        return False
    if get_lower(row_nr, col_nr, input) == '#':
        return False
    if get_lower_right(row_nr, col_nr, input) == '#':
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


def get_grid(input):
    grid_with_seats = []
    row_size = len(input)
    for row_nr, row in enumerate(input):
        column_size = len(row)
        new_row = []
        for col_nr, item in enumerate(row):
            if item == 'L':
                if all_adjacent_free(row_nr, col_nr, input, column_size, row_size):
                    new_row.append('#')
                else:
                    new_row.append(item)
            elif item == '#':
                if get_nr_of_occupied_adjacent(row_nr, col_nr, input, column_size, row_size) >= 4:
                    new_row.append('L')
                else:
                    new_row.append(item)
            else:
                new_row.append(item)

        grid_with_seats.append(''.join(new_row))
    #print('\n'.join(grid_with_seats))
    #print('-------------------------------------------')

    return grid_with_seats


def count_nr_of(item, data):
    data_as_string = ''.join(data)
    return data_as_string.count(item)


def run_with_data(data, expected_occupied_count, expected_counter):
    # data = INPUT.split('\n')
    new_grid = ''
    old_grid = data
    running = True
    counter = 0
    while (running):
        new_grid = get_grid(old_grid)
        counter += 1
        if new_grid == old_grid:
            running = False
        old_grid = new_grid

    print('counter=' + str(counter))
    occupied_seats = count_nr_of('#', new_grid)
    print('occupied_seats=' + str(occupied_seats))
    assert counter == expected_counter
    assert occupied_seats == expected_occupied_count


def main():
    # Small data
    # expected = ['#.#L.L#.##', '#LLL#LL.L#', 'L.#.L..#..', '#L##.##.L#', '#.#L.LL.LL', '#.#L#L#.##', '..L.L.....', '#L#L##L#L#', '#.LLLLLL.L', '#.#L#L#.##']
    # print('expected', expected)
    # print('new_grid', new_grid)
    # assert new_grid == expected
    data = INPUT.split('\n')
    run_with_data(data, 37, 6)

    data = util.read_data('11.data')
    run_with_data(data, 2338, 87)


if __name__ == '__main__':
    main()
