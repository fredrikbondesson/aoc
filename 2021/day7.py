import sys

INPUT = """16,1,2,0,4,2,7,1,2,14"""

"""
    Move from 16 to 2: 14 fuel
    Move from 1 to 2: 1 fuel
    Move from 2 to 2: 0 fuel
    Move from 0 to 2: 2 fuel
    Move from 4 to 2: 2 fuel
    Move from 2 to 2: 0 fuel
    Move from 7 to 2: 5 fuel
    Move from 1 to 2: 1 fuel
    Move from 2 to 2: 0 fuel
    Move from 14 to 2: 12 fuel
"""
def get_sum_for_position(pos, data, cost = None):
    sum_ = 0
    for item in data:
        difference = abs(item - pos)
        if cost == None:
            sum_ = sum_ + difference
        else:
            sum_ = sum_ + cost[difference]

    return sum_


def get_smallest(data, cost=None):
    smallest = sys.maxsize

    # TODO Perhaps generate magic number 100000
    for pos in range(100000):
        res = get_sum_for_position(pos, data, cost)
        smallest = min(res, smallest)

    return smallest


def main():
    print('Part1:')
    data = list(map(int, INPUT.split(',')))

    # This costs a total of 37 fuel.
    # This is the cheapest possible outcome; more expensive outcomes 
    # include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).
    res = get_sum_for_position(3, data)
    print(res)
    assert res == 39

    res = get_sum_for_position(10, data)
    print(res)
    assert res == 71

    res = get_sum_for_position(2, data)
    print(res)
    assert res == 37

    smallest = get_smallest(data)
    print(smallest)
    assert smallest == 37

    data = list(map(int, open('2021/day7.txt').read().split(',')))
    smallest = get_smallest(data)
    print(smallest)
    assert smallest == 339321

    print('Part2:')
    cost = []
    sum = 0
    for a in range(0, 10000000):
        cost.append(a + sum)
        sum = a + sum
    print('Generated cost list')
    
    data = list(map(int, INPUT.split(',')))
   
    res = get_sum_for_position(2, data, cost)
    print(res)
    assert res == 206

    smallest = get_smallest(data, cost)
    print(smallest)
    assert smallest == 168

    data = list(map(int, open('2021/day7.txt').read().split(',')))
    smallest = get_smallest(data, cost)
    print(smallest)
    assert smallest == 95476244

"""As it turns out, crab submarine engines don't burn fuel at a constant rate. 
Instead, each change of 1 step in horizontal position costs 1 more unit of fuel 
than the last: 
the first step costs 1, 
the second step costs 2, 
the third step costs 3, and so on.

As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes 5:

    Move from 16 to 5: 66 fuel
    Move from 1 to 5: 10 fuel
    Move from 2 to 5: 6 fuel
    Move from 0 to 5: 15 fuel
    Move from 4 to 5: 1 fuel
    Move from 2 to 5: 6 fuel
    Move from 7 to 5: 3 fuel
    Move from 1 to 5: 10 fuel
    Move from 2 to 5: 6 fuel
    Move from 14 to 5: 45 fuel

This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead."""

if __name__ == '__main__':
    main()
