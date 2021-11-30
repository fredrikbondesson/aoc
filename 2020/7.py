import util

INPUT = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
# In the above rules, the following options would be available to you:
# A bright white bag, which can hold your shiny gold bag directly.
# A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
# A dark orange bag, which can hold bright white and muted yellow bags, either of which
#   could then hold your shiny gold bag.
# A light red bag, which can hold bright white and muted yellow bags, either of which
#   could then hold your shiny gold bag.
# So, in this example, the number of bag colors that can eventually contain at least
# one shiny gold bag is 4.

INPUT2 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain no other bags.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


# PART 2
# Consider again your shiny gold bag and the rules from the above example:
#  faded blue bags contain 0 other bags.
#  dotted black bags contain 0 other bags.
#  vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
#  dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
#
# So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it)
# plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

# Here's another example:
# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.
# In this example (INPUT3), a single shiny gold bag must contain 126 other bags.
INPUT3 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


def parse_row(row, rows):
    # print('parse_row::::: ' + row)
    if 'contain no other bags' in row:
        return False
    # print(row)

    splitted = row.split(' ')
    current = splitted[0] + ' ' + splitted[1]
    #print("current: " + current)
    if current == 'shiny gold':
        return False

    pos1 = 5
    pos2 = 6
    while True:
        try:
            next = splitted[pos1] + ' ' + splitted[pos2]    # 9,10  13,14
            # print("next: " + next)
        except IndexError:
            # print(e)
            return False

        if next == 'shiny gold':
            # print('We found shiny gold')
            return True

        for new_row in rows:
            if new_row.startswith(next):
                # print('now look for ' + next)
                contains_gold = parse_row(new_row, rows)
                if contains_gold:
                    return True
                else:
                    pos1 += 4
                    pos2 += 4


def run_part1_with_data(rows, expected_count, log=False):
    counter = 0
    for row in rows:
        contains_shiny_gold = parse_row(row, rows)
        if contains_shiny_gold:
            util.log(row + " contains shiny gold", log)
            counter += 1
            util.log('', log)

    assert counter == expected_count
    util.log('------------------------------------------------------', log)


def count_bags(row, rows):
    # print('count_bags::::: ' + row)
    if 'contain no other bags' in row:
        # print("End here for row " + row)
        return 0

    splitted = row.split(' ')
    total_nr_of_bags = 0
    pos1 = 5
    pos2 = 6
    nr_of_bags_pos = 4
    while True:
        try:
            # TODO Assume: nr_of_bags < 10
            nr_of_bags = int(splitted[nr_of_bags_pos])
            next = splitted[pos1] + ' ' + splitted[pos2]    # 9,10  13,14
        except IndexError:
            return total_nr_of_bags

        for new_row in rows:
            if new_row.startswith(next):
                # print('now look for ' + next)
                nr_of_bags = nr_of_bags + nr_of_bags * count_bags(new_row, rows)
                total_nr_of_bags += nr_of_bags
                print(next + " -> " + str(nr_of_bags))
                pos1 += 4
                pos2 += 4
                nr_of_bags_pos += 4

    print("return here " + str(nr_of_bags))
    return nr_of_bags


def run_part2_with_data(rows, expected_count, log=False):
    counter = 0
    for row in rows:
        if row.startswith('shiny gold'):
            counter = count_bags(row, rows)

    print('counter=' + str(counter))
    assert counter == expected_count
    util.log('------------------------------------------------------', log)


def main():
    # rows = INPUT.split('\n')
    # run_part1_with_data(rows, expected_count=4, log=True)

    # rows = INPUT2.split('\n')
    # run_part1_with_data(rows, expected_count=3, log=True)

    # rows = util.read_data('7.data')
    # run_part1_with_data(rows, expected_count=348, log=False)

    rows = INPUT.split('\n')
    run_part2_with_data(rows, expected_count=32, log=True)

    rows = INPUT3.split('\n')
    run_part2_with_data(rows, expected_count=126, log=True)

    rows = util.read_data('7.data')
    run_part2_with_data(rows, expected_count=18885, log=True)


if __name__ == '__main__':
    main()
