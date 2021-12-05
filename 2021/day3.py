from typing import DefaultDict
import util

"""
day 3 part2
oxygen generator rating

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

11110
10110
10111
10101
11100
10000
11001

10110
10111
10101
10000

10110
10111
10101

10110
10111

In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.

10111

CO2 scrubber rating
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

00100
01111
00111
00010
01010

01010
01111

In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.

Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

"""

INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def get_gamma_and_epsilon_rate(columns: list):
    gamma_rate = []
    epsilon_rate = []
    for item in columns:
        # print(columns[item])
        # print(len([x for x in columns[item] if x==0]))
        # print(len([x for x in columns[item] if x==1]))
        if len([x for x in columns[item] if x==0]) > len([x for x in columns[item] if x==1]):
            gamma_rate.append('0')
            epsilon_rate.append('1')
        else:
            gamma_rate.append('1')
            epsilon_rate.append('0')

    gamma_binary_as_string = ''.join(gamma_rate)
    epsilon_binary_as_string = ''.join(epsilon_rate)

    return int(gamma_binary_as_string, 2), int(epsilon_binary_as_string, 2)


def convert_to_columns(input):
    columns = DefaultDict(list)
    for row in input:
        for col,value in enumerate(row):
            columns[col].append(int(value))

    return columns


def get_part2(rows: list):
    most = rows
    least = rows
    for col_idx in range(0, len(rows[0])):
        most = get_most_common(most, col_idx)
        least = get_least_common(least, col_idx)

    return most, least


def get_most_common(rows: list, col_idx):
    if len(rows) == 1:
        return rows
    column = []
    for row in rows:
        column.append(row[col_idx])

    ones = [idx for idx,x in enumerate(column) if x=='1']
    zeros = [idx for idx,x in enumerate(column) if x=='0']
    most_common = []
    use_this = ones

    if len(zeros)>len(ones):
        use_this = zeros

    for i in use_this:
        most_common.append(rows[i])

    return most_common


def get_least_common(rows: list, col_idx):
    if len(rows) == 1:
        return rows
    column = []
    for row in rows:
        column.append(row[col_idx])

    ones = [idx for idx,x in enumerate(column) if x=='1']
    zeros = [idx for idx,x in enumerate(column) if x=='0']
    use_this = zeros
    least_common = []

    if len(zeros) > len(ones):
        use_this = ones

    for i in use_this:
        least_common.append(rows[i])

    return least_common


if __name__ == '__main__':
    print('Part1:')
    columns = convert_to_columns(INPUT.splitlines())
    gamma_rate, epsilon_rate = get_gamma_and_epsilon_rate(columns)
    power_consumption = gamma_rate * epsilon_rate
    print(f'gamma_rate={gamma_rate} epsilon_rate={epsilon_rate} power_consumption={power_consumption}')
    assert power_consumption == 198

    data = util.read_data('2021/day3.txt')
    columns = convert_to_columns(data)
    gamma_rate, epsilon_rate = get_gamma_and_epsilon_rate(columns)
    power_consumption = gamma_rate * epsilon_rate
    print(f'gamma_rate={gamma_rate} epsilon_rate={epsilon_rate} power_consumption={power_consumption}')
    assert power_consumption == 2498354

    print('Part2:')
    most, least = get_part2(INPUT.splitlines())
    assert most == ['10111']
    most_as_int = int(most[0], 2)
    assert most_as_int == 23

    assert least == ['01010']
    least_as_int = int(least[0], 2)
    assert least_as_int == 10

    assert most_as_int * least_as_int == 230

    most, least = get_part2(data)
    most_as_int = int(most[0], 2)
    least_as_int = int(least[0], 2)

    print(most_as_int * least_as_int)
    assert most_as_int * least_as_int == 3277956
