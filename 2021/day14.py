from collections import Counter


INPUT="""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


# The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
# The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
# The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.

# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB


# def insert(source_str, insert_str, pos):
#     return source_str[:pos]+insert_str+source_str[pos:]


def run_part1(template, rules, nr_of_steps):
    input = template
    for nr in range(nr_of_steps):
        res = run_inner_part1(input, rules)
        input = res
        print(f'After step {nr+1}: len={len(res)}')

    return res


def run_inner_part1(template, rules):
    data = []
    for idx in range(len(template) - 1):
        data.append(template[idx])
        d = template[idx:idx+2]
        insert_char = rules[d]
        data.append(insert_char)
        #print(f'After step {nr+1}: {res}')

    data.append(template[-1])

    return ''.join(data)


def main():
    rules = {}
    template = INPUT.split('\n', maxsplit=1)[0]
    for item in INPUT.strip().split('\n')[2:]:
        rule, val = item.split(' -> ')
        rules[rule] = val

    res = run_part1(template, rules, 1)
    assert res == 'NCNBCHB', f'{res} != {"NCNBCHB"}'

    res = run_part1(template, rules, 4)
    assert res == 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'

    res = run_part1(template, rules, 10)
    assert len(res) == 3073
    res = Counter(res)
    max_char = max(res, key = res.get)
    min_char = min(res, key = res.get)
    print(f'Diff max-min: {res[max_char] - res[min_char]}')
    assert res[max_char] - res[min_char] == 1588
    res = Counter(res)
    max_char = max(res, key = res.get)
    min_char = min(res, key = res.get)
    print(f'Diff max-min: {res[max_char] - res[min_char]}')
    res = run_part1(template, rules, 10)

    assert len(res) == 3073
    res = Counter(res)
    max_char = max(res, key = res.get)
    min_char = min(res, key = res.get)
    print(f'Diff max-min: {res[max_char] - res[min_char]}')
    assert res[max_char] - res[min_char] == 1588

    # res = run_part1(template, rules, 40)

    print('Part1')
    data = open('2021/day14.txt').read().strip().split('\n')
    template = data[0]
    rules = {}
    for item in data[2:]:
        rule, val = item.split(' -> ')
        rules[rule] = val

    res = run_part1(template, rules, 10)
    res = Counter(res)
    max_char = max(res, key = res.get)
    min_char = min(res, key = res.get)
    print(f'Diff max-min: {res[max_char] - res[min_char]}')
    assert res[max_char] - res[min_char] == 2874


if __name__ == '__main__':
    main()
