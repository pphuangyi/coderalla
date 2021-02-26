#! /usr/bin/python3.7

import sys
from math import sqrt
from functools import reduce

def simplify(a, b):
    m, n = a, b 
    while True:
        r = m % n
        if r == 0:
            break
        m = n
        n = r

    return a // n, b // n


def foo(s, n, mod=None):
    arr = [s + i for i in range(1, n + 1)]
    for i in range(1, n + 1):
        while i > 1:
            start = 0
            for j in range(start, n):
                a, b = simplify(i, arr[j])
                if a < i:
                    i, arr[j], start = a, b, j + 1
                    break
    if mod is not None:
        prod = reduce(lambda a, b: (a * b) % mod, arr)
    else:
        prod = reduce(lambda a, b: (a * b), arr)
    
    return int(prod)


def invert(a, M):


if __name__ == '__main__':

    # So M is indeed a prime
    M = 1e9 + 7

    aha = int((sqrt(M) + 1) / 6) + 1
    print(aha)


    for k in range(1, aha):
        a = 6 * k - 1
        b = a + 2

        if M % a == 0:
            print(a)
        if M % b == 0:
            print(b)


    
