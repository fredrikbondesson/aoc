from collections import Counter, defaultdict
from typing import Tuple


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


def get_as_char_pair_and_how_many(template:str)->dict:
    res = defaultdict(int)
    for idx in range(len(template) - 1):
        chars = template[idx] + template[idx + 1]
        if chars in res:
            res[chars] += 1
        else:
            res[chars] = 1

    return res


def run(template:str, rules:dict, nr_of_steps: int)->Tuple(int, int):
    input = get_as_char_pair_and_how_many(template)

    for nr in range(nr_of_steps):
        res, letters = run_step(input, rules)
        input = res
        # print(f'After step {nr+1}: len={len(res)}')
        # print(f'res={res}')
        # print(f'letters={letters}')
    
    # Never adds the last char, so do it here
    letters[template[-1]] += 1

    max_letter = max(letters, key=letters.get)
    min_letter = min(letters, key=letters.get)

    return letters[max_letter], letters[min_letter]


def run_step(template:str, rules:dict)->Tuple[dict, dict]:
    res = defaultdict(int)
    letters  = defaultdict(int)
    for key, val in template.items():
        insert_char = rules.get(key)
        first_char = key[0]
        if insert_char:
            insert_chars = first_char + insert_char
            res[insert_chars] += 1 * val
            letters[first_char] += 1 * val
            letters[insert_char] += 1 * val
            insert_chars = insert_char + key[1]
            res[insert_chars] += 1 * val

    return res, letters
    

def main():
    insertion_rules = {}
    template = INPUT.split('\n', maxsplit=1)[0]
    for item in INPUT.strip().split('\n')[2:]:
        rule, val = item.split(' -> ')
        insertion_rules[rule] = val

    max, min = run(template, insertion_rules, 10)
    print(max, min)
    print(f'Diff max-min: {max - min}')
    assert max - min == 1588

    # B 2192039569602 H 3849876073
    max, min = run(template, insertion_rules, 40)
    print(max, min)
    print(f'Diff max-min: {max - min}')
    assert max - min == 2188189693529

    data = open('2021/day14.txt').read().strip().split('\n')
    template = data[0]
    insertion_rules = {}
    for item in data[2:]:
        rule, val = item.split(' -> ')
        insertion_rules[rule] = val

    max, min = run(template, insertion_rules, 10)
    print(max, min)
    print(f'Diff max-min: {max - min}')
    assert max - min == 2874

    max, min = run(template, insertion_rules, 40)
    print(max, min)
    print(f'Diff max-min: {max - min}')
    assert max - min == 5208377027195


if __name__ == '__main__':
    main()
