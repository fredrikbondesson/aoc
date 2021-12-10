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


def get_as_length_dict_length(letters_as_one_string):
    dict_ = defaultdict(list)
    for letters in letters_as_one_string.split(' '):
        dict_[len(letters)].append("".join(sorted(letters)))

    return dict_


def get_top_segment(dict_):
    p1 = get_pattern_for_nr(1, dict_)
    p7 = get_pattern_for_nr(7, dict_)
    return set(p7) - set(p1)


def get_pattern_for_nr(nr, dict_):
    for _key, value in dict_.items():
        if len(value[0]) == 2 and nr == 1:
            return value[0]
        if len(value[0]) == 4 and nr == 4:
            return value[0]
        if len(value[0]) == 3 and nr == 7:
            return value[0]
        if len(value[0]) == 7 and nr == 8:
            return value[0]

    return None


def get_pattern_for_six(dict_):
    one = get_pattern_for_nr(1, dict_)
    set_one = set(one)
    for item in dict_[6]:
        if not set_one.issubset(set(item)):
            # print(f'Compare {one} with {item}-> this is pattern for number six')
            return item


def get_pattern_for_three(dict_):
    seven = get_pattern_for_nr(7, dict_)
    set_seven = set(seven)
    for item in dict_[5]:
        if set_seven.issubset(set(item)):
            # print(f'Compare {seven} with {item}-> this is pattern for number three')
            return item


def get_pattern_for_nine(dict_):
    four = get_pattern_for_nr(4, dict_)
    top_segment = get_top_segment(dict_)
    set_four_plus_top = set(four).union(top_segment)
    for item in dict_[6]:
        # print(f'Compare {four} with {item}-> this is pattern for number nine')
        if len(set(item).difference(set_four_plus_top)) == 1:
            return item


def get_pattern_for_five(dict_, six, three):
    six_set = set(six)
    for item in dict_[5]:
        if item == three:
            continue
        # print(f'Compare {six} with {item}-> this is pattern for number five')
        if len(set(item).difference(six_set)) == 0:
            return item


def get_pattern_for_two(dict_, three, five):
    for item in dict_[5]:
        if item == three or item == five:
            continue
        # print(f'{item}-> this is pattern for number two')
        return item


def get_pattern_for_zero(dict_, p6, p9):
    for item in dict_[6]:
        if item != p6 and item != p9:
            # print(f'{item} -> this is pattern for number zero')
            return item


def get_set_as_string(set_):
    return "".join(set_)


def create_mapping(dict_):
    one = get_pattern_for_nr(1, dict_)
    four = get_pattern_for_nr(4, dict_)
    seven = get_pattern_for_nr(7, dict_)
    eight = get_pattern_for_nr(8, dict_)
    six = get_pattern_for_six(dict_)
    three = get_pattern_for_three(dict_)
    nine = get_pattern_for_nine(dict_)
    zero = get_pattern_for_zero(dict_, six, nine)
    five = get_pattern_for_five(dict_, six, three)
    two = get_pattern_for_two(dict_, three, five)

    return {zero:0, one: 1, two: 2, three: 3, four: 4, five:5, six:6, seven:7, eight:8, nine:9}


def part_2(data, exp_value):
    summa = 0
    for row in data:
        signal_pattern, output_value = row.split('|')
        print(signal_pattern)
        print(output_value.lstrip())
        output_value = output_value.lstrip()
        dict_ = get_as_length_dict_length(signal_pattern)
        # print(dict_)

        mapping = create_mapping(dict_)
        print(mapping)
        multiple = 1000
        for val in output_value.split(' '):
            # print(val)
            for pattern, nr in mapping.items():
                if set(val) == set(pattern):
                    # print(nr * multiple)
                    summa += nr * multiple
                    multiple = multiple/10
       # print(int(summa))

    assert int(summa) == exp_value

"""
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
sorted -> 
abcdefg bcdef acdfg abcdf abd abcdef bcdefg abef abcdeg ab | bcdef abcdf bcdef abcdf

8) 7 st:
abcdefg

(0,6,9) 6 st:
abcdef
bcdefg
abcdeg

(2,3,5) 5 st:
bcdef
acdfg
abcdf

(4) 4 st:
abef

(7) 3 st:
abd

(1)2 st:
ab

jämför 7 - 1 => skillnaden ger top segmentet abd - ab = d

jämför alla med 6 mot 1 den som inte har båda 1:ans segment borde då vara bcdefg=6 sedan jämför vi 6 med 8 vilket borde ge oss övre högra segmentet bcdefg - abcdefg -> a

jämför 7 med alla med fem den som har alla gemensamt borde vara 3 abd -> abcdf abcdf -> 3

lägg till top segmentet till 4an och jämför sedan med alla med 6 och den med bara en skillnad borde då vara 9an  abef + d => abdef - abcdef = abcdef -> 9
och sedan finns det bara en 6a kvar vilket är abcdeg->0

jämför 6an med de två femmor som finns kvar, den med minst skillnad borde vara 5   bcdefg - bcdef->g  eller bcdefg - acdfg->be  => bcdef borde vara 5

"""
def main():

    part_2(INPUT.split('\n'), exp_value=61229)

    data = util.read_data('2021/day8.txt')
    part_2(data, exp_value=1027422)

if __name__ == '__main__':
    main()
