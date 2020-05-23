#!/usr/bin/python

import sys
from collections import defaultdict

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    if cache is None or cache[0] == 0:
        cache = defaultdict(int)
        cache[0] = 1
        cache[1] = 1
        cache[2] = 2
        cache[3] = 4
        cache[4] = 7

    if cache[n] == 0:
        cache[n] = eating_cookies(
            n - 3, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 1, cache)

    return cache[n]


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
#             ways=eating_cookies(num_cookies), n=num_cookies))
#     else:
#         print('Usage: eating_cookies.py [num_cookies]')
print(eating_cookies(5, [0, 0, 0, 0, 0]))
