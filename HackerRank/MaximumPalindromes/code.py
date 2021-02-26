#!/usr/bin/python3.7

import sys
from fractions import Fraction
import random
from time import time

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


def initialize(s, mod):
    records = [[0 for _ in range(26)]]
    for c in s:
        idx = ord(c) - ord('a')
        row = records[-1].copy()
        row[idx] += 1
        records.append(row)
    
    # Get factorial and factorial inverses
    factorials, factorial_inverses = [1], [1]
    for i in range(1, len(s) + 1):
        f = (factorials[-1] * i) % mod
        _, i, _ = extended_Euclidean_algorithm(mod, f)
        factorials.append(f)
        factorial_inverses.append(i)

    return records, factorials, factorial_inverses

    
def answerQuery(l, r, records, factorial, factorial_inverses, mod):
    record = [records[r][i] - records[l - 1][i] for i in range(26)]
    num_odds = sum([r % 2 == 1 for r in record])
    
    # print(record)
    result = factorials[sum([r // 2 for r in record])]
    # print(result)
    for r in record:
        result = (result * factorial_inverses[r // 2]) % mod
        
    return int((result * max(1, num_odds)) % mod)



if __name__ == '__main__':


    input_index = sys.argv[1]
    input_fname = f'data/input{input_index}.txt'
    output_fname = f'data/output{input_index}.txt'

    queries = []
    with open(input_fname, 'r') as handle:
        s = handle.readline().strip()

        q = int(handle.readline().strip())

        for q_itr in range(q):
            l, r = list(map(int, handle.readline().rstrip().split()))
            queries.append([l, r])
    
    results = []
    with open(output_fname, 'r') as handle:
        for line in handle:
            r = int(line.strip())
            results.append(r)



    print(f'{len(queries)}')

    mod = int(1e9 + 7)
    records, factorials, factorial_inverses = initialize(s, mod)

    n = 0
    for f, i in zip(factorials[:10], factorial_inverses[:10]):
        print(f'{n}: {f}, {i}')
        print((f * i) % mod)
        n += 1


    for i, (l, r) in enumerate(queries):
        r = answerQuery(l, r, records, factorials, factorial_inverses, mod)
        print(f'{i}: {r}, {results[i]}')

