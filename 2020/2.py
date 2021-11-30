import sys
import util
# For example, suppose you have the following list:

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

# Each line gives the password policy and then the password. 
# The password policy indicates the lowest and highest number of times a given letter 
# must appear for the password to be valid. For example, 1-3 a means that the password 
# must contain a at least 1 time and at most 3 times.

# In the above example, 2 passwords are valid. The middle password, cdefg, is not; 
# it contains no instances of b, but needs at least 1. The first and third passwords are valid: 
# they contain one a or nine c, both within the limits of their respective policies.

# 2nd part:
# Each policy actually describes two positions in the password, 
# where 1 means the first character, 2 means the second character, and so on. 
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
# Exactly one of these positions must contain the given letter. 
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

# Given the same example list from above:
#    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
#    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
#    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.


INPUT = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
def extract_letter(text):
    return text.split()[1][:-1]


def extract_min_max_rule(text):
    min, max = text.split()[0].split('-')
    return(int(min), int(max))


def extract_password(text):
    return text.split()[2]


def get_nr_of_correct_part1(lines):
    correct = 0
    for line in lines:
        if line:
            letter = extract_letter(line)
            min, max = extract_min_max_rule(line)
            password = extract_password(line)

            matches = password.count(letter)
            if matches>=min and matches<=max:
                correct+=1

    return correct


def get_nr_of_correct_part2(lines):
    correct = 0
    for line in lines:
        letter = extract_letter(line)
        idx1, idx2 = extract_min_max_rule(line)
        password = extract_password(line)
        # TODO Improve
        if password[idx1 - 1] == letter and password[idx2 - 1] != letter or password[idx1 - 1] != letter and password[idx2 - 1] == letter:
            correct+=1
        else:
            print('Not correct ' + line)

    return correct


def main(*argv):
    # Part 1
    correct = 0
    correct = get_nr_of_correct_part1(INPUT.split('\n'))
    print(correct)
    assert(correct == 2)

    lines = util.read_data('2.data')
    correct = get_nr_of_correct_part1(lines)
    print(correct)
    assert(correct == 586)

    # Part 2
    correct = get_nr_of_correct_part2(INPUT.split('\n'))
    print(correct)
    assert(correct == 1)

    correct = get_nr_of_correct_part2(lines)
    print(correct)
    assert(correct == 352)


if __name__ == '__main__':
    print("args=%s" %(sys.argv))
    main(sys.argv)
