import util
#from typing import tuple

INPUT2 = """1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25"""

INPUT = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def get_all_two_sums(numbers):
    sums = []
    start_idx = 0
    while start_idx < len(numbers) - 1:
        for end_idx in range(start_idx + 1, len(numbers)):
            sums.append(numbers[start_idx] + numbers[end_idx])
        start_idx += 1

    return sums


def check_XMAS_validity(numbers, preamble=5):
    idx = 0
    while idx + preamble < len(numbers):
        sums = get_all_two_sums(numbers[idx:idx + preamble])
        if numbers[idx + preamble] not in sums:
            print(f'Invalid data at line {idx + preamble + 1} : {numbers[idx + preamble]}')
            return numbers[idx + preamble]

        idx += 1
    return None


def find_min_max_in_contiguous_set(data, sum) -> tuple((int, int)):
    start_idx = 0

    while True:
        idx = 1
        items = [data[start_idx]]
        calc_sum = data[start_idx]
        while start_idx + idx < len(data):
            
            item = data[start_idx + idx]
            items.append(item)
            calc_sum = calc_sum + item
            
            if calc_sum == sum:
                return min(items), max(items)
            
            idx += 1

        start_idx += 1


def main():
    data = list(map(int, INPUT2.split()))
    data.append(26)
    res = check_XMAS_validity(data, preamble=25)
    print(res)
    assert res == None

    data = list(map(int, INPUT2.split()))
    data.append(49)
    res = check_XMAS_validity(data, preamble=25)
    print(res)
    assert res == None

    data = list(map(int, INPUT2.split()))
    data.append(100)
    res = check_XMAS_validity(data, preamble=25)
    print(res)
    assert res == 100

    data = list(map(int, INPUT2.split()))
    data.append(50)
    res = check_XMAS_validity(data, preamble=25)
    print(res)
    assert res == 50    

    data = list(map(int, INPUT.split()))
    res = check_XMAS_validity(data, preamble=5)
    print(res)
    assert res == 127
    res = find_min_max_in_contiguous_set(data, 127)
    assert res == (15, 47)

    data = list(map(int, open('2020/9.data').read().split()))
    res = check_XMAS_validity(data, preamble=25)
    print(res)
    assert res == 373803594

    res = find_min_max_in_contiguous_set(data, 373803594)
    print(res)
    assert res == (15104298, 36048062)
    assert 15104298 + 36048062 == 51152360


if __name__ == '__main__':
    main()