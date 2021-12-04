from typing import DefaultDict
import util

"""
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.

"""

"""
--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of 
determining whether a string is naughty or nice. 
None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in 
    the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), 
    but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter 
    between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    - qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) 
      and a letter that repeats with exactly one letter between them (zxz).
    - xxyxx is nice because it has a pair that appears twice and a letter 
      that repeats with one between, even though the letters used by each rule overlap.
    - uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat 
      with a single letter between them.
    - ieodomkazucvgmuy is naughty because it has a repeating letter with one 
      between (odo), but no pair that appears twice.

How many strings are nice under these new rules?
"""

vowels = 'aeiou'
invalid = ['ab', 'cd', 'pq', 'xy']


def check_vowels(input: str) -> bool:
    count = 0
    for c in input:
        if c in vowels:
            count += 1
    return count >= 3


def check_invalid(input: str) -> bool:
    for i in invalid:
        if i in input:
            return True
    return False


def check_appears_twice(input: str) -> bool:
    for i in range(len(input) - 1):
        if input[i] == input[i+1]:
            return True
    return False


def check_string(input: str) -> bool:
    # print('Checking:', input)
    if not check_vowels(input):
        return False
    
    if check_invalid(input):
        return False

    if not check_appears_twice(input):
        return False

    return True


def check_string_part2(input: str) -> bool:
    # print('Checking part2:', input)
    if not check_appears_twice_with_one_between(input):
        return False

    if not check_pair_of_letter_appears_twice(input):
        return False

    return True


def check_pair_of_letter_appears_twice(input: str) -> bool:
    for i in range(len(input) - 2):
        pair = input[i:i+2]
        if pair in input[i+2:]:
            return True

    return False


def check_appears_twice_with_one_between(input: str) -> bool:
    for i in range(len(input) - 2):
        if input[i] == input[i+2]:
            return True
    return False


def main():
    print("Part 1:")

    ok = check_string('ugknbfddgicrmopn')
    assert ok == True

    ok = check_string('aaa')
    assert ok == True
        
    ok = check_string('jchzalrnumimnmhp')
    assert ok == False
    
    ok = check_string('dvszwmarrgswjxmb')
    assert ok == False

    ok = check_string('haegwjzuvuyypxyu')
    assert ok == False

    data = util.read_data('2015/day5.txt')

    count = 0
    for line in data:
        if check_string(line):
            count += 1
    print(count)
    assert count == 255

    print("Part 2:")
    
    ok = check_string_part2('qjhvhtzxzqqjkmpb')
    assert ok == True

    ok = check_string_part2('xxyxx')
    assert ok == True

    ok = check_string_part2('uurcxstgmygtbstg')
    assert ok == False

    ok = check_string_part2('ieodomkazucvgmuy')
    assert ok == False

    count = 0
    for line in data:
        if check_string_part2(line):
            count += 1

    print(count)
    assert count == 55


if __name__ == '__main__':
    main()