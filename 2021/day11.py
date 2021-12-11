import util
import timeit

INPUT="""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


nr_of_flashes = 0


def get_item_from(row_nr, col_nr, data):
    if row_nr < 0:
        return -1
    if col_nr < 0:
        return -1
    try:
        return data[row_nr][col_nr]
    except IndexError:
        return -1
        

# def check_all_neighbours(row_nr, col_nr, data):
#     xy_neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# 
#     for idx, (x_delta, y_delta) in enumerate(xy_neighbours):
#         print(idx, x_delta, y_delta)


def increase_neighbours_with_one(row_nr, col_nr, data):
    xy_neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbour_is_set = False
    for idx, (x_delta, y_delta) in enumerate(xy_neighbours):
        current = get_item_from(row_nr + y_delta, col_nr + x_delta, data)
        if current > 0:
            data[row_nr + y_delta][col_nr + x_delta] += 1
            if data[row_nr + y_delta][col_nr + x_delta] > 9:
                neighbour_is_set = True

    return neighbour_is_set


def run_one_step(data):
    # Increase with one
    for row_nr, row in enumerate(data):
        for col_nr, current_value in enumerate(row):
            row[col_nr] = current_value + 1

    # Increase  until no more flashings
    done = False
    counter = 0
    global nr_of_flashes
    while not done:
        done = True
        counter += 1
        for row_nr, row in enumerate(data):
            for col_nr, current_value in enumerate(row):
                if current_value > 9:
                    neighbour_is_set = increase_neighbours_with_one(row_nr, col_nr, data)
                    if neighbour_is_set:
                        done = False
                    data[row_nr][col_nr] = 0
                    nr_of_flashes = nr_of_flashes +  1

def get_as_list_of_lists(data):
    rows = []
    for row in data:
        buf = []
        for nr in row:
            buf.append(int(nr))

        rows.append(buf)
    return rows


def run_with_example_data():
    print('run_with_example_data')
    print('Part 1:')

    rows = get_as_list_of_lists(INPUT.split('\n'))

    global nr_of_flashes
    nr_of_flashes = 0
    run_one_step(rows)
    assert rows == [
        [6,5,9,4,2,5,4,3,3,4],
        [3,8,5,6,9,6,5,8,2,2],
        [6,3,7,5,6,6,7,2,8,4],
        [7,2,5,2,4,4,7,2,5,7],
        [7,4,6,8,4,9,6,5,8,9],
        [5,2,7,8,6,3,5,7,5,6],
        [3,2,8,7,9,5,2,8,3,2],
        [7,9,9,3,9,9,2,2,4,5],
        [5,9,5,7,9,5,9,6,6,5],
        [6,3,9,4,8,6,2,6,3,7],
    ]
    run_one_step(rows)
    assert rows == [
        [8,8,0,7,4,7,6,5,5,5],
        [5,0,8,9,0,8,7,0,5,4],
        [8,5,9,7,8,8,9,6,0,8],
        [8,4,8,5,7,6,9,6,0,0],
        [8,7,0,0,9,0,8,8,0,0],
        [6,6,0,0,0,8,8,9,8,9],
        [6,8,0,0,0,0,5,9,4,3],
        [0,0,0,0,0,0,7,4,5,6],
        [9,0,0,0,0,0,0,8,7,6],
        [8,7,0,0,0,0,6,8,4,8],
    ]
    run_one_step(rows)
    run_one_step(rows)
    run_one_step(rows)
    run_one_step(rows)
    run_one_step(rows)
    run_one_step(rows)
    run_one_step(rows)
    run_one_step(rows)

    # After step 10:
    assert rows == [
        [0,4,8,1,1,1,2,9,7,6],
        [0,0,3,1,1,1,2,0,0,9],
        [0,0,4,1,1,1,2,5,0,4],
        [0,0,8,1,1,1,1,4,0,6],
        [0,0,9,9,1,1,1,3,0,6],
        [0,0,9,3,5,1,1,2,3,3],
        [0,4,4,2,3,6,1,1,3,0],
        [5,5,3,2,2,5,2,3,5,0],
        [0,5,3,2,2,5,0,6,0,0],
        [0,0,3,2,2,4,0,0,0,0],
    ]
    assert nr_of_flashes == 204
    
    for nr in range(90):
        run_one_step(rows)

    # After step 100:
    assert rows == [
        [0,3,9,7,6,6,6,8,6,6],
        [0,7,4,9,7,6,6,9,1,8],
        [0,0,5,3,9,7,6,9,3,3],
        [0,0,0,4,2,9,7,8,2,2],
        [0,0,0,4,2,2,9,8,9,2],
        [0,0,5,3,2,2,2,8,7,7],
        [0,5,3,2,2,2,2,9,6,6],
        [9,3,2,2,2,2,8,9,6,6],
        [7,9,2,2,2,8,6,8,6,6],
        [6,7,8,9,9,9,8,7,6,6],
    ]
    assert nr_of_flashes == 1656

    print('Part 2:')
    all_flashing_nr = 0
    all_flashing = [[0]*10]*10
    for nr in range(1, 101):
        run_one_step(rows)
        if rows == all_flashing and all_flashing_nr == 0:
            all_flashing_nr = nr

    assert all_flashing_nr == 95


def run_with_real_data():
    print('run_with_real_data')
    print('Part 1:')
    data = util.read_data('2021/day11.txt')
    global nr_of_flashes
    nr_of_flashes = 0

    rows = get_as_list_of_lists(data)

    for nr in range(1, 101):
        run_one_step(rows)

    # After step 100:
    assert rows == [
        [0, 0, 0, 0, 6, 6, 9, 8, 9, 7], 
        [0, 0, 0, 8, 8, 2, 3, 3, 0, 9], 
        [0, 0, 8, 8, 2, 2, 3, 6, 0, 0],
        [0, 8, 8, 2, 2, 2, 3, 6, 0, 0], 
        [6, 8, 2, 2, 2, 3, 5, 2, 4, 0],
        [7, 3, 2, 2, 2, 4, 1, 1, 2, 2], 
        [1, 4, 2, 2, 3, 6, 1, 1, 1, 6], 
        [1, 4, 2, 3, 5, 1, 1, 1, 1, 5], 
        [3, 4, 4, 5, 1, 1, 1, 1, 1, 5], 
        [2, 3, 1, 1, 6, 1, 1, 1, 1, 9]
        ]
    # print(nr_of_flashes)
    assert nr_of_flashes == 1694
    assert nr == 100

    print('Part 2:')
    nr_of_flashes = 0
    data = util.read_data('2021/day11.txt')

    rows = get_as_list_of_lists(data)

    all_flashing = [[0]*10]*10
    for nr in range(1, 500):
        run_one_step(rows)
        if rows == all_flashing:
            all_flashing_nr = nr
            break

    assert all_flashing_nr == 346


def main():
    start = timeit.default_timer()
    run_with_example_data()
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    start = timeit.default_timer()
    run_with_real_data()
    stop = timeit.default_timer()
    print('Time: ', stop - start)


if __name__ == '__main__':
    main()