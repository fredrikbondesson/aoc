#INPUT = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""

from collections import defaultdict
import util

INPUT = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

mapping_length_number = {2:1, 4:4, 3:7, 7:8}

def get_number_from_length(length):
    if length in mapping_length_number.keys():
        return mapping_length_number[length]
    return None

def part1(rows):
    res = defaultdict(int)
    for row in rows:
        data = row[row.find('|') + 2:]
        items = data.split(' ')
        for item in items:
            length = len(item)
            number = get_number_from_length(length)
            if number:
                res[number] = res[number] + 1

    return res

# Part 2
"""
 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
"""

mapping = {
    0:['a','b', 'c', 'g','e','d'],
    1 : ['a','b'],
    2:['d', 'a', 'f','g','c'],
    3:['d','f','c','a','b'],
    4:['e','f','a', 'b'],
    5:['d','f','b','c', 'e'],
    6:['d','f','b','c', 'g'],
    7:['d', 'a','b'],
    9:['d','f','b','c','a','e'],
    8:['a','b','c','d','e', 'f', 'g'],
    }

def get_as_number(letters_as_one_string):
    check = [x for x in letters_as_one_string]
    # print('Check:' + str(check))
    for nr in range(9):
        if set(check) == set(mapping[nr]):
            return nr

"""So, the unique signal patterns would correspond to the following digits:

    acedgfb: 8
    cdfbe: 5
    gcdfa: 2
    fbcad: 3
    dab: 7
    cefabd: 9
    cdfgeb: 6
    eafb: 4
    cagedb: 0
    ab: 1

Then, the four digits of the output value can be decoded:

    cdfeb: 5
    fcadb: 3
    cdfeb: 5
    cdbaf: 3

Therefore, the output value for this entry is 5353."""

"""
    fdgacbe cefdb cefbgd gcbe: 8394
    fcgedb cgb dgebacf gc: 9781
    cg cg fdcagb cbg: 1197
    efabcd cedba gadfec cb: 9361
    gecf egdcabf bgf bfgea: 4873
    gebdcfa ecba ca fadegcb: 8418
    cefg dcbef fcge gbcadfe: 4548
    ed bcgafe cdgba cbgef: 1625
    gbdfcae bgc cg cgb: 8717
    fgae cfgab fg bagce: 4315

    Adding all of the output values in this larger example produces 61229.
"""

INPUT2 = """fdgacbe cefdb cefbgd gcbe
fcgedb cgb dgebacf gc
cg cg fdcagb cbg
efabcd cedba gadfec cb
gecf egdcabf bgf bfgea
gebdcfa ecba ca fadegcb
cefg dcbef fcge gbcadfe
ed bcgafe cdgba cbgef
gbdfcae bgc cg cgb
fgae cfgab fg bagce"""
def main():
    print('Part1:')
    rows = INPUT.split('\n')
    res = part1(rows)
    print(res)
    print(sum(res.values()))
    assert sum(res.values()) == 26

    rows = util.read_data('2021/day8.txt')
    res = part1(rows)
    print(res)
    print(sum(res.values()))
    assert sum(res.values()) == 397

    res = get_as_number('cdfeb')
    print(res)
    assert res == 5

    res = get_as_number('fcadb')
    print(res)
    assert res == 3

    buf = []
    for row in 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab cdfeb fcadb cdfeb cdbaf'.split(' '):
        print(row)
        print(sorted(row))
        buf.append("".join(sorted(row)))

    print(' '.join(buf))

    # for row in INPUT2.split('\n'):
    #     the_list = [x for x in row.split(' ')]
    #     for apa in the_list:
    #         res = get_as_number(apa)
    #         if res == None:
    #             res = get_number_from_length(len(apa))
    #         if res == None:
    #             print(f'Not found {apa}')
    #         # print(res)


if __name__ == '__main__':
    main()
