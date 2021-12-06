import collections


INPUT = """3,4,3,1,2"""


# Should use something like this
# def compute(s: str) -> int:
#     numbers = collections.Counter(int(line) for line in s.strip().split(','))

#     for d in range(256):
#         numbers2 = collections.Counter({8: numbers[0], 6: numbers[0]})
#         numbers2.update({k - 1: v for k, v in numbers.items() if k > 0})
#         numbers = numbers2
#         print(f'Day {d}: {sum(numbers.values())} nr of fishes')

#     return sum(numbers.values())

def step(day_nr_, data) -> int:
    new_dict = {}

    new_dict[6] = data[0] * 1
    new_dict[8] = data[0] * 1
    new_dict[0] = data[1] * 1
    new_dict[1] = data[2] * 1
    new_dict[2] = data[3] * 1
    new_dict[3] = data[4] * 1
    new_dict[4] = data[5] * 1
    new_dict[5] = data[6] * 1
    new_dict[6] = new_dict[6] + data[7] * 1
    new_dict[7] = data[8] * 1

    data.clear()
    data.update(new_dict)
    summa = get_sum(data)
    # print(f'Day {day_nr_}: {summa} nr of fishes')
    return summa


def get_sum(the_dict):
    summa = 0
    for val in the_dict.values():
        summa += val
    return summa


def calculate_for_nr_of_days(nr_of_days, data) -> int:
    day = 1
    while day <= nr_of_days:
        nr_of_fishes = step(day, data)
        day += 1

    return nr_of_fishes


def numbers_to_dict(numbers):
    the_dict = collections.defaultdict(lambda: 0)
    for nr in numbers:
        the_dict[nr] = the_dict[nr] + 1

    return the_dict


def main():
    data = list(map(int, INPUT.split(',')))

    as_dict = numbers_to_dict(data)
    res = calculate_for_nr_of_days(18, as_dict)
    print(res)
    assert res == 26

    as_dict = numbers_to_dict(data)
    res = calculate_for_nr_of_days(80, as_dict)
    print(res)
    assert res == 5934

    as_dict = numbers_to_dict(data)
    res = calculate_for_nr_of_days(256, as_dict)
    print(res)
    assert res == 26984457539

    data = list(map(int, open('2021/day6.txt').read().split(',')))
    as_dict = numbers_to_dict(data)
    res = calculate_for_nr_of_days(80, as_dict)
    print(res)
    assert res == 383160

    as_dict = numbers_to_dict(data)
    res = calculate_for_nr_of_days(256, as_dict)
    print(res)
    assert res == 1721148811504


if __name__ == '__main__':
    main()
