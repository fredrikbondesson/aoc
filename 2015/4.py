from typing import DefaultDict
import hashlib
# import util

"""To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. 
The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number 
in decimal. To mine AdventCoins, you must find Santa the lowest positive number 
(no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

    If your secret key is abcdef, the answer is 609043, 
    because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), 
    and it is the lowest such number to do so.
    If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting 
    with five zeroes is 1048970; that is, 
    the MD5 hash of pqrstuv1048970 looks like 000006136ef....
"""

"""--- Part Two ---

Now find one that starts with six zeroes.
"""

def calculate_smallest(key: str, nr_of_leading_zeros = 5) -> int: 
    for i in range(10000000000):
        if hashlib.md5((key+ str(i)).encode('utf-8')).hexdigest()[:nr_of_leading_zeros] == "0" * nr_of_leading_zeros:
            return i


def main():
    print("Part 1:")
    hash = calculate_smallest('abcdef')
    print(hash)
    assert hash == 609043

    hash = calculate_smallest('pqrstuv')
    print(hash)
    assert hash == 1048970

    hash = calculate_smallest('iwrupvqb')
    print(hash)
    assert hash == 346386

    print("Part 2:")
    hash = calculate_smallest('iwrupvqb', nr_of_leading_zeros = 6)
    print(hash)
    assert hash == 9958218


if __name__ == '__main__':
    main()