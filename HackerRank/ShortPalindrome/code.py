
import math
import os
import random
import re
import sys

mod = 1e9 + 7

def first_strictly_greater(arr, k, start=0):
    f, t = start, len(arr)
    while f < t:
        m = (f + t) // 2
        if arr[m] <= k:
            f = m + 1
        else:
            t = m
    return f

# def foo(p1, p2):
#     count = 0
#     f = 0
#     for i in range(len(p1)):
#         f = first_strictly_greater(p2, p1[i], start=f)
#         t = f
#         for j in range(i + 1, len(p1)):
#             t = first_strictly_greater(p2, p1[j], start=t)
#             l = t - f
#             count = (count + l * (l - 1) // 2) % mod
#             
#     return count

def foo(p1, p2):
    count = 0
    f = 0
    for i in range(len(p1)):
        for j in range(i + 1, len(p1)):
			a = p2 > p1[i]
			count = (count + len(a)) % mod
			
    return count

def shortPalindrome(s):
    mydict = {}
    for i, c in enumerate(s):
        if c in mydict:
            mydict[c].append(i)
        else:
            mydict[c] = [i]
    
    count = 0    
    for c1 in mydict:
        for c2 in mydict:
            if c1 == c2:
                l = len(mydict[c1])
                count = (count + l * (l - 1) * (l - 2) * (l - 3) // 24) % mod
            else:
                a = foo(mydict[c1], mydict[c2])
                print(f'{c1}, {c2}: {a}')
                count = (count + a) % mod
        
    return int(count)
        

if __name__ == '__main__':
	input_idx = sys.argv[1]
	input_fname = f'input_{input_idx}'
	
	with open(input_fname, 'r') as handle:
		s = handle.readline()
		print(s)
	
	count = shortPalindrome(s)
	print(count)
