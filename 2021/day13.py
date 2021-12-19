import util
import timeit


INPUT="""6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

def fold_horizontal(in_data, pos):
    rows = []
    max_x = len(in_data[0])
    for _ in range(0, pos):
        rows.append(['.'] * (max_x))
    print(f'max_x={max_x}')
    for row_nr, row in enumerate(rows):
        for col_nr, _ in enumerate(row):
            # print(row_nr, col_nr)
            #if row_nr == 750 and col_nr == 10:
            #    import pdb;pdb.set_trace()
            current_value = in_data[row_nr][col_nr]
            rows[row_nr][col_nr] = current_value
            from_folding = in_data[len(in_data) - row_nr - 1][col_nr]
            # print('get value from row ' + str(len(in_data) - row_nr - 1) + ' colnr='+str(col_nr) + ' into row ' + str(row_nr) + ' colnr=' + str(col_nr) + ' val=' + from_folding)
            if from_folding == '#':
                rows[row_nr][col_nr] = from_folding

    assert len(rows) == pos
    for row in rows:
        assert len(row) == max_x

    return rows


def fold_vertical(in_data, pos):
    rows = []
    max_y = len(in_data)
    for _ in range(0, max_y):
        rows.append(['.'] * (pos))
    print(f'max_y={max_y} pos={pos} ')
    for row_nr, row in enumerate(rows):
        for col_nr, _ in enumerate(row):
            #if row_nr == 750 and col_nr == 10:
            #    import pdb;pdb.set_trace()
            current_value = in_data[row_nr][col_nr]
            rows[row_nr][col_nr] = current_value
            from_folding = in_data[row_nr][len(in_data[row_nr]) - col_nr - 1]
            # print('get value from row ' + str(row_nr) + ' colnr=' + str(len(in_data[row_nr]) - col_nr - 1) + " into row " + str(row_nr) + ' col=' + str(col_nr) + ' val=' + from_folding)
            if from_folding == '#':
                rows[row_nr][col_nr] = from_folding

    assert len(rows) == len(in_data)
    for row in rows:
        assert len(row) == pos
    return rows


def check_vertical(in_data, pos):
    for row in in_data:
        if row[pos] == '#':
            print( f"check_vertical pos={pos}")
            print(row)
            assert False

def check_horizontal(in_data, pos):
    for letter in in_data[pos]:
        if letter == '#':
            print( f"check_horizontal pos={pos}")
            print(in_data[pos])
            #assert False


def calculate_dots(in_data):
    nr_of_dots = 0
    for row in in_data:
        nr_of_dots += len([x for x in row if x=='#'])

    return nr_of_dots


def run_with_data(in_data, nr_of_folds = None):
    rows = []
    xy = []
    folds = []
    for input_row in in_data:
        if 'fold along' not in input_row and input_row != '':
            x, y = input_row.split(',')
            xy.append((int(x), int(y)))
        else:
            if input_row != '':
                folds.append(input_row)

    max_x = max([x[0] for x in xy])
    max_y = max([x[1] for x in xy])

    print(f'max_x={max_x} max_y={max_y}')

    rows = []
    for _ in range(0, max_y + 1):
        rows.append(['.'] * (max_x + 1))

    for (x, y) in xy:
        rows[y][x] = '#'

    #for row in rows:
    #    print(''.join(row))

    res = rows
    #print_data(res)
    counter = 0
    for fold in folds:
        where, pos = (fold.split('='))
        pos = int(pos)
        if where == 'fold along x':
            print(f'fold_vertical at x={pos}')
            # if pos != int(len(res[0]) / 2):
            #    print(pos, int(len(res[0]) / 2))
            #    assert False
            # check_vertical(res, int(pos))
            res = fold_vertical(res, pos)
            #for row in res:
            #    print(row)
        elif where == 'fold along y':
            print(f'fold_horizontal at y={pos}')
            # if int(pos) != int(len(res) / 2):
            #    print(pos, int(len(res) / 2))
            #    assert False
            # check_horizontal(res, int(pos))
            res = fold_horizontal(res, int(pos))
            #for row in res:
            #    print(row)
        counter +=1
        nr_of_points = calculate_dots(res)
        for row_idx, row in enumerate(res):
            for col_idx, letter in enumerate(row):
                if letter == '#':
                    print(col_idx, row_idx)
                    pass

        print(f'counter={counter} nr_of_points={nr_of_points}')

        if nr_of_folds and nr_of_folds<=counter:
            break

        # 1 684
        # 2 569
        # 3 470
        # 4 391
        # 5 329
        # 6 270
        # 7 226
        # 8 192
        # 9 168
        # 10 140
        # 11 117
        # 12 98
        # print_data(res, fold_x=None, fold_y=None)
    # print_data(res, fold_x=None, fold_y=None)

    # for row_idx, row in enumerate(res):
    #     for col_idx, letter in enumerate(row):
    #         if letter == '#':
    #             print(col_idx, row_idx)
    #             pass
    return calculate_dots(res)


def print_data(data, fold_x=None, fold_y=None):
    res_string = ""
    for row in data:
        for letter in row:
            #print(''.join(row))
            #res_string += ("█" if letter == '#' else ".")
            res_string += ("#" if letter == '#' else ".")

        res_string += '\n'

    print(res_string)


def main():
    # start = timeit.default_timer()
    # res = run_with_data(INPUT.split('\n'), nr_of_folds = 1)
    # assert res == 17
    # stop = timeit.default_timer()
    # print('Time: ', stop - start)

    # start = timeit.default_timer()
    # res = run_with_data(INPUT.split('\n'))
    # assert res == 16 # 17 efter första vikningen och 16 efter andra
    # stop = timeit.default_timer()
    # print('Time: ', stop - start)

    start = timeit.default_timer()
    data = util.read_data('2021/day13.txt')
    # # parse_input('2021/day13.txt')

    # res = run_with_data(data, nr_of_folds = 1)
    # assert res == 684
    # stop = timeit.default_timer()
    # print('Time: ', stop - start)

    res = run_with_data(data, nr_of_folds = 2)
    assert res == 569
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    # res = run_with_data(data)
    # #assert res == 98
    # stop = timeit.default_timer()
    # print('Time: ', stop - start)

if __name__ == '__main__':
    main()
