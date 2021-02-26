#!/usr/bin/python3.7

import sys
import random
from time import time
from functools import reduce


def extended_Euclidean_algorithm(a, b):
    """
    Make sure a and b are both integer
    Wikipedia page: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    """
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    while True:
        q, r = r0 // r1, r0 % r1 # In plain Euclidean algorithm, we don't save quotient(q)
        if r == 0:
            break
        s = s0 - q * s1 
        t = t0 - q * t1 
        r0, r1 = r1, r
        s0, s1 = s1, s
        t0, t1 = t1, t

    # s1 * a + t1 * b = r1
    return s1, t1, r1


def foo(arr, mod):
    """
    Better to make sure [mod] is a prime integer. 
    Remember that a number written using scientific notation is a float!
    """

    if len(arr) == 0:
        return 1

    max_entry = max(arr)
    
    # ================= process the numerator ================= 
    prod_numerator = 1
    for i in range(max_entry + 1, sum(arr) + 1):
        prod_numerator *= i
        if prod_numerator >= mod:
            prod_numerator %= mod

    # ================= process the denominator ================= 
    brr = arr.copy()
    brr.remove(max_entry)
    prod_denominator = 1
    for number in brr:
        for i in range(1, number + 1):
            prod_denominator *= i
            if prod_denominator >= mod:
                prod_denominator %= mod 

    # get the inverse of prod_denominator
    _, t, _ = extended_Euclidean_algorithm(mod, prod_denominator)

    return (t * prod_numerator) % mod
    

def foo_reduced(arr, mod):
    """
    Better to make sure [mod] is a prime integer. 
    Remember that a number written using scientific notation is a float!
    """

    if len(arr) == 0:
        return 1

    max_entry = max(arr)
    
    # ================= process the numerator ================= 
    prod_numerator = reduce(lambda a, b: (a * b) % mod, [1] + list(range(max_entry + 1, sum(arr) + 1)))

    # ================= process the denominator ================= 
    brr = arr.copy()
    brr.remove(max_entry)
    prod_denominator = 1
    for number in brr:
        p = reduce(lambda a, b: (a * b) % mod, range(1, number + 1))
        prod_denominator = (prod_denominator * p) % mod

    # get the inverse of prod_denominator
    _, t, _ = extended_Euclidean_algorithm(mod, prod_denominator)

    return (t * prod_numerator) % mod
    

if __name__ == '__main__':



    length_lower, length_upper = 0, 26
    lower, upper = 5000, 20000
    mod = int(1e9 + 7)

    # ============================= Start Timing =============================     
    time0 = time()

    count = 0
    num_runs = 1000
    while count < num_runs:
        length = random.randint(length_lower, length_upper)
        arr = [random.randint(lower, upper) for _ in range(length)]
        if sum(arr) > 100000:
            continue
        # result = foo(arr, mod)
        result = foo_reduced(arr, mod)
        print(f'{count}: {arr} \n{result}\n')
        count += 1

    time1 = time()
    # ============================= End Timing =============================     
    
    time_elapsed = time1 - time0
    print(f'{time_elapsed:.3f}')

