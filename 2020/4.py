import util
import re

INPUT = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


"""
    PART1

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

    The first passport is valid - all eight fields are present.
    The second passport is invalid - it is missing hgt (the Height field).
    The third passport is interesting; the only missing field is cid,
    so it looks like data from North Pole Credentials, not a passport at all!
    Surely, nobody would mind if you made the system temporarily ignore missing cid fields.
    Treat this "passport" as valid.

    The fourth passport is missing two fields, cid and byr.
    Missing cid is fine, but missing any other field is not, so this passport is invalid.

    According to the above rules, your improved system would report 2 valid passports.

    Count the number of valid passports - those that have all required fields.
    Treat cid as optional. In your batch file, how many passports are valid?
    """


def is_valid(data):
    valid_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    if valid_keys.issubset(set(data.keys())):
        return True

    return False


# PART2
INVALID_PASSPORTS = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

VALID_PASSPORTS = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


def valid_byr(value): return '1920' <= value <= '2002'
def valid_iyr(value): return '2010' <= value <= '2020'
def valid_eyr(value): return '2020' <= value <= '2030'
def valid_hgt(value): return (value[-2:] == 'cm' and '150'<= value[:-2] <= '193' or
                              value[-2:] == 'in' and '59'<= value[:-2] <= '76')
def valid_hcl(value): return len(value) == 7 and re.fullmatch('#[0-9,a-f]+', value)
def valid_ecl(value): return value in ('amb', 'blu', 'brn', 'gry' ,'grn', 'hzl', 'oth')
def valid_pid(value): return len(value) == 9 and value.isdigit()


def valid_fields(data):
    return (valid_byr(data['byr']) and valid_iyr(data['iyr']) and valid_eyr(data['eyr']) and
            valid_hgt(data['hgt']) and valid_hcl(data['hcl']) and valid_ecl(data['ecl']) and valid_pid(data['pid']) )


def get_passport_data(rows):
    data = []
    passport = {}
    for row in rows:
        if row == '':
            data.append(passport)
            passport = {}
        else:
            for item in row.split():
                key, value = item.split(':')
                passport[key] = value

    return data


def test_with_data(rows, exp_valid_passports, exp_valid_fields):
    counter = 0
    counter_valid_fields = 0
    res = get_passport_data(rows)
    for passport in res:
        if is_valid(passport):
            counter +=1
            if valid_fields(passport):
                counter_valid_fields +=1
    print(counter)
    print(counter_valid_fields)
    assert counter == exp_valid_passports
    assert counter_valid_fields == exp_valid_fields


def main():
    test_with_data(INPUT.split('\n'), 2, 2)
    test_with_data(INVALID_PASSPORTS.split('\n'), 4, 0)
    test_with_data(VALID_PASSPORTS.split('\n'), 4, 4)

    rows = util.read_data('4.data')
    test_with_data(rows, 202, 137)


if __name__ == '__main__':
    main()
