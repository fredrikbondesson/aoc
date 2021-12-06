#import util


INPUT = """3,4,3,1,2"""


def step(day_nr,  data) -> int:
    nrs = len(data)
    for idx in range(0, nrs):
        fish_timer = data[idx]
        if fish_timer == 0:
            data.append(8)
            data[idx] = 6
        else:
            data[idx] -= 1

    print(f'After {day_nr} day(s): {len(data)} nr of fishes')
    return len(data)


def calculate_for_nr_of_days(nr_of_days, data) -> int:
    day = 1
    while day <= nr_of_days:
        nr_of_fishes = step(day, data)
        # print(len(data))
        day += 1

    return nr_of_fishes


def main():
    print('Part1:')
    data = list(map(int, INPUT.split(',')))
    res = calculate_for_nr_of_days(18, data)
    assert res == 26

    data = list(map(int, INPUT.split(',')))
    res = calculate_for_nr_of_days(80, data)
    assert res == 5934

    print('')
    data = list(map(int, open('2021/day6.txt').read().split(',')))
    res = calculate_for_nr_of_days(80, data)
    assert res == 383160

    # print('Part2:')
    # This solution is way to slow for Part2 :)


if __name__ == '__main__':
    main()
