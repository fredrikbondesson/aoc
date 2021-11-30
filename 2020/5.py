import util
import re

# For example, consider just the first seven characters of FBFBBFFRLR:

#     Start by considering the whole range, rows 0 through 127.
#     F means to take the lower half, keeping rows 0 through 63.
#     B means to take the upper half, keeping rows 32 through 63.
#     F means to take the lower half, keeping rows 32 through 47.
#     B means to take the upper half, keeping rows 40 through 47.
#     B keeps rows 44 through 47.
#     F keeps rows 44 through 45.
#     The final F keeps the lower of the two, row 44.

# For example, consider just the last 3 characters of FBFBBFFRLR:
#     Start by considering the whole range, columns 0 through 7.
#     R means to take the upper half, keeping columns 4 through 7.
#     L means to take the lower half, keeping columns 4 through 5.
#     The final R keeps the upper of the two, column 5.

# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

# Here are some other boarding passes:
#     BFFFBBFRRR: row 70, column 7, seat ID 567.
#     FFFBBBFRRR: row 14, column 7, seat ID 119.
#     BBFFBBFRLL: row 102, column 4, seat ID 820.

def get_row_nr(row_data, min_row=0, max_row=127):
    if len(row_data) == 0:
        return min_row
    if row_data[0] == 'F':
        return get_row_nr(row_data[1:], min_row=min_row, max_row=min_row - 1 + (max_row-min_row + 1)/2)
    elif row_data[0] == 'B':
        return get_row_nr(row_data[1:], min_row=min_row + (max_row-min_row + 1)/2, max_row=max_row)

def get_column_nr(column_data, min_col=0, max_col=7):
    if len(column_data) == 0:
        return int(min_col)
    if column_data[0] == 'L':
        return get_column_nr(column_data[1:], min_col=min_col, max_col=min_col - 1 + (max_col-min_col + 1)/2)
    elif column_data[0] == 'R':
        return get_column_nr(column_data[1:], min_col=min_col + (max_col-min_col + 1)/2, max_col=max_col)

def get_seat_id(data):
    res1 = get_row_nr(data[:-3])
    res2 = get_column_nr(data[-3:])
    return int(get_row_nr(data[:-3]) * 8 + get_column_nr(data[-3:]))

def get_missing_in_range(ids):
    counted_id = ids[0]
    for id in sorted(ids):
        if id != counted_id:
            print(counted_id)
            return counted_id
        counted_id +=1

def main():
    assert get_seat_id('FBFBBFFRLR') == 357
    assert get_seat_id('BFFFBBFRRR') == 567
    assert get_seat_id('FFFBBBFRRR') == 119
    assert get_seat_id('BBFFBBFRLL') == 820

    rows = util.read_data('5.data')
    ids = []
    for row in rows:
        ids.append(get_seat_id(row))

    #print(sorted(ids))
    print(max(ids))
    assert max(ids) == 813

    assert get_missing_in_range(sorted(ids)) == 612


if __name__ == '__main__':
    main()