#!/usr/bin/python3.7

import os
import sys

def bonetrousle(n, k, b):
    if k == b:
        return list(range(1, k + 1))

    # ============================== find prefix ============================== 
    prefix_length = (2 * k * b - b * b + b - 2 * n) // (2 * (k - b))
    if prefix_length == b:
        return list(range(1, b + 1))
    prefix = list(range(1, prefix_length + 1))

    n -= (prefix_length + 1) * prefix_length // 2 + (b - prefix_length) * prefix_length
    b -= prefix_length
    k -= prefix_length

    # ============================== find split ============================== 
    b_l, b_r = (b + 1) // 2, b // 2
    l_min = (1 + b_l) * b_l // 2
    r_max = (2 * k - b_r + 1) * b_r // 2
    lower = max(l_min, n - r_max)
    
    l_max = lambda l: (2 * l + 1 - b_l) // 2
    r_min = lambda l: (2 * l + 1 + b_r) // 2 
    
    
    t = 2 * lower + (b_l - 1) * b_l
    if t % (2 * b_l) == 0:
        l = t // (2 * b_l)
    else:
        l = t // (2 * b_l) + 1
        
    if (l >= b_l) and (l <= n - b_r) and (l_max(l) + r_min(l) <= n):
        L = list(range(l - b_l + 1, l + 1))
        R = bentrousle(n - l_max(l) - l * b_r, k - l, b_r)
        suffix = L + [x + l for x in R]
    else:
        l = (2 * (n - lower) - (b_r + 1) * b_r) // (2 * b_r)
        L = bentrousle(n - r_min(l), l, b_l)
        R = list(range(l + 1, l + b_r + 1))
        suffix = L + R
        
    return prefix + [x + prefix_length for x in suffix]
    
    

if __name__ == '__main__':

    index = sys.argv[1]
    input_fname = f'data/input{index}.txt'

    with open(input_fname, 'r') as handle:
        t = int(handle.readline().strip())
        for line in handle:
            n, k, b = list(map(int, line.strip().split()))
            print(f'n={n}, k={k}, b={b}')
            # result = bonetrousle(n, k, b)
            # print(f'n = {n}, N = {sum(result)}')

