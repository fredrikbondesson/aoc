from typing import DefaultDict
import util

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

    # print(gamma_rate, epsilon_rate)
    binary1 = '0b' + ''.join(gamma_rate)
    binary2 = '0b' + ''.join(epsilon_rate)
    return int(binary1,2), int(binary2,2)


def convert_to_columns(input):
    columns = DefaultDict(list)
    for row in input:
        for col,value in enumerate(row):
            columns[col].append(int(value))

    return columns


def get_part2(rows: list):
    import pdb
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