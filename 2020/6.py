from collections import defaultdict
import util


INPUT = """abc

a
b
c

ab
ac

a
a
a
a

b
"""
# PART 1
# This list represents answers from five groups:
# The first group contains one person who answered "yes" to 3 questions: a, b, and c.
# The second group contains three people; combined,
#  they answered "yes" to 3 questions: a, b, and c.
# The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
# The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
# The last group contains one person who answered "yes" to only 1 question, b.
# In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

# PART 2
# This list represents answers from five groups:
# In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
# In the second group, there is no question to which everyone answered "yes".
# In the third group, everyone answered yes to only 1 question, a. Since some people did not
# answer "yes" to b or c, they don't count.
# In the fourth group, everyone answered yes to only 1 question, a.
# In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
# In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.


def test_part1(data, expected_count):
    res = 0
    group_answers = set()
    for row in data:
        if row == '':
            res += len(group_answers)
            group_answers = set()
        for letter in row:
            group_answers.update(letter)

    print(res)
    assert res == expected_count


def count_questions_with_all_yes(answers, nr_of_people_in_group):
    # print(answers)
    # print(nr_of_people_in_group)
    res = 0
    for key in answers:
        if answers[key] == nr_of_people_in_group:
            res += 1
    return res


def test_part2(data, expected_count):
    res = 0
    group_answers = defaultdict(lambda: 0)
    nr_of_people_in_group = 0
    for row in data:
        if row == '':
            res += count_questions_with_all_yes(group_answers, nr_of_people_in_group)
            group_answers = defaultdict(lambda: 0)
            nr_of_people_in_group = 0
        else:
            nr_of_people_in_group += 1
        for letter in row:
            group_answers[letter] += 1

    print(res)
    assert res == expected_count


def main():
    test_part1(INPUT.split('\n'), expected_count=11)

    rows = util.read_data('6.data')
    test_part1(rows, expected_count=6748)

    test_part2(INPUT.split('\n'), expected_count=6)
    rows = util.read_data('6.data')
    test_part2(rows, expected_count=3445)


if __name__ == '__main__':
    main()
