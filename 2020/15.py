import time

# INPUT = [0, 3, 6]
# CORRECT = [0, 3, 6, 0, 4-1, 5-2, 1, 0, 8-4, 0]
# 1:  0
# 2:  3
# 3:  6
# 4:  0
# 5:  4-1=3
# 6:  5-2=3
# 7:  6-5=1
# 8:  0
# 9:  8-4=4
# 10: 0
# 11: 10-8=2
# 12: 0
# ...
# 2020: 436

# Here are a few more examples:
#     Given the starting numbers 1,3,2, the 2020th number spoken is 1.
#     Given the starting numbers 2,1,3, the 2020th number spoken is 10.
#     Given the starting numbers 1,2,3, the 2020th number spoken is 27.
#     Given the starting numbers 2,3,1, the 2020th number spoken is 78.
#     Given the starting numbers 3,2,1, the 2020th number spoken is 438.
#     Given the starting numbers 3,1,2, the 2020th number spoken is 1836.


# PART1 - Really SLOW :( use PART2 instead
def get_last_index_for(value, values, start_index):
    idx = start_index
    while idx >= 0:
        if value == values[idx]:
            return idx
        idx -= 1

    return -1


def check(pos, values):
    current_value = values[pos]
    idx = get_last_index_for(current_value, values, len(values)-2)
    if idx == -1:
        return 0
    return pos - idx


def part1_with_input(values, exp_value, end_index=2019):
    index = len(values) - 1
    while index < end_index:
        res = check(index, values)
        values.append(res)
        index += 1

    print(values[-1])
    assert exp_value == values[-1]


# PART2
def check_part2(current_value, current_idx, value_with_idx):
    if current_value in value_with_idx:
        found_idx = value_with_idx[current_value]
        if current_idx == found_idx:
            return 0
        else:
            value_with_idx[current_value] = current_idx
            return current_idx - found_idx
    else:
        value_with_idx[current_value] = current_idx
        return 0

    print("Should never happen")
    assert False


def part2_with_input(value_with_idx, current_value, exp_value, end_index=2019):
    index = len(value_with_idx) - 1
    while index < end_index:
        current_value = check_part2(current_value, index, value_with_idx)
        index += 1

    print(current_value)
    assert exp_value == current_value


def main():

    # NOTE This solution is really slow
    values = [0, 3, 6]
    start_time = time.time()
    part1_with_input(values, 436)
    elapsed_time = time.time() - start_time
    print('Operation took=%s seconds' % (elapsed_time))
    # values = [1, 3, 2]
    # part1_with_input(values, 1)

    # values = [2, 1, 3]
    # part1_with_input(values, 10)

    # values = [1, 2, 3]
    # part1_with_input(values, 27)

    # values = [2, 3, 1]
    # part1_with_input(values, 78)

    # values = [3, 2, 1]
    # part1_with_input(values, 438)

    # values = [3, 1, 2]
    # part1_with_input(values, 1836)

    values = [6, 4, 12, 1, 20, 0, 16]
    part1_with_input(values, 475)

    value_idx = {0: 0, 3: 1, 6: 2}
    values = [0, 3, 6]
    start_time = time.time()
    part2_with_input(value_idx, current_value=values[-1], exp_value=436)
    elapsed_time = time.time() - start_time
    print('Operation took=%s seconds' % (elapsed_time))
    value_idx = {0: 0, 3: 1, 6: 2}
    values = [0, 3, 6]
    start_time = time.time()
    part2_with_input(value_idx, current_value=values[-1], exp_value=175594, end_index=30000000-1)
    elapsed_time = time.time() - start_time
    print('Operation took=%s seconds' % (elapsed_time))

#     Given 0,3,6, the 30000000th number spoken is 175594.
#     Given 1,3,2, the 30000000th number spoken is 2578.
#     Given 2,1,3, the 30000000th number spoken is 3544142.
#     Given 1,2,3, the 30000000th number spoken is 261214.
#     Given 2,3,1, the 30000000th number spoken is 6895259.
#     Given 3,2,1, the 30000000th number spoken is 18.
#     Given 3,1,2, the 30000000th number spoken is 362.

    value_idx = {6: 0, 4: 1, 12: 2, 1: 3, 20: 4, 0: 5, 16: 6}
    values = [6, 4, 12, 1, 20, 0, 16]
    start_time = time.time()
    part2_with_input(value_idx, current_value=values[-1], exp_value=11261, end_index=30000000-1)
    elapsed_time = time.time() - start_time
    print('Operation took=%s seconds' % (elapsed_time))


if __name__ == '__main__':
    main()
