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


if __name__ == '__main__':
    main()
