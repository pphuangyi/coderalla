#!/usr/bin/python3.7


import math
import os
import random
import re
import sys
from time import time


def lena_sort(arr):
    if len(arr) == 0:
        return [], 0
    if len(arr) == 1:
        return arr, 0

    pivot = arr[0]
    less, more = [], []
    for a in arr[1:]:
        if a < pivot:
            less.append(a)
        else:
            more.append(a)
    
    less_sorted, less_comparisons = lena_sort(less)
    more_sorted, more_comparisons = lena_sort(more)
    arr_sorted = less_sorted + [pivot] + more_sorted
    comparisons = less_comparisons + more_comparisons + len(arr) - 1

    return arr_sorted, comparisons


def get_min_arr(length, start):
    """
    get the array with integer 0, ..., n-1 such that
    it requires the minimum number of comparison
    when applying QuickSort.
    """
    if length == 0:
        return []
    if length == 1:
        return [0]
    
    memo = [(0, length)]
    while len(memo) < length:
        new_memo = []
        for m in memo:
            if isinstance(m, int):
                new_memo.append(m)
            else:
                s, l = m
                middle = s + (l - 1) // 2
                new_memo.append(middle)
                s_less, l_less = s, (l - 1) // 2
                s_more, l_more = middle + 1, l // 2
                if l_less == 1:
                    new_memo.append(s_less)
                elif l_less > 1:
                    new_memo.append((s_less, l_less))
                if l_more == 1:
                    new_memo.append(s_more)
                elif l_more > 1:
                    new_memo.append((s_more, l_more))
        memo = new_memo
    
    return [start + m for m in memo]


def rec(length, comparisons, first):

    if length == 0:
        return []
    if length == 1:
        return [first]
    
    # length of increasing sequence it could tolerate
    prefix_length = 0
    remaining = length
    while True:
        tmp = remaining - 1
        if comparisons - tmp >= smallest[tmp]:
            prefix_length += 1
            comparisons -= tmp
            remaining = tmp
        else:
            break
    prefix = [first + p for p in range(prefix_length)]
    if prefix_length == length:
        return prefix

#    print(f'prefix length = {prefix_length}')
    
    # split
    length -= prefix_length
    comparisons -= remaining - 1
    first = first + prefix_length
    
    for less in range((length + 1) // 2):
        more = length - 1 - less
        max_more, min_more = more * (more - 1) // 2, smallest[more]
        max_less, min_less = less * (less - 1) // 2, smallest[less]
        lower = max(min_less, comparisons - max_more)
        upper = min(max_less, comparisons - min_more)
        if upper >= lower:
            break
#     print(f'\nlength={length}, comparison={comparisons}, less={less}')
#     print(f'\tless = {less}, more = {more}')
#     print(f'\tless half: ({min_less}, {max_less})')
#     print(f'\tmore half: ({min_more}, {max_more})')
#     print(f'\t(lower, upper) = ({lower}, {upper})')  
    pivot = first + less

    if lower == comparisons - max_more:     # comparisons_more = max_more
        # print('lower == comparisons - max_more')
        comparisons_less = lower        
        A = rec(less, comparisons_less, first)
        B = list(range(pivot + 1, pivot + 1 + more))
    elif upper == comparisons - min_more:   # comparisons_more = min_more
        # print('upper == comparisons - min_more')
        comparisons_less = upper        
        A = rec(less, comparisons_less, first)
        B = get_min_arr(more, pivot + 1)
    else: # upper == max_less
        # print('upper == max_less')
        comparisons_less = upper
        comparisons_more = comparisons - comparisons_less
        A = list(range(first, first + less))
        B = rec(more, comparisons_more, pivot + 1)

    return prefix + [pivot] + A + B   



if __name__ == '__main__':
    
    index = sys.argv[1]
    input_fname = f'data/input{index}.txt'
    output_fname = f'data/output{index}.txt'


    C = []
    smallest = [0, 0]
    with open(input_fname, 'r') as handle:
        queries = int(handle.readline().strip())
        count = 0
        time0 = time()
        for line in handle:
            l, c = list(map(int, line.strip().split())) 
            for length in range(len(smallest), l + 1):
                if length % 2 == 0:
                    s = smallest[length // 2 - 1] + smallest[length // 2]
                else:
                    s = 2 * smallest[length // 2]
                smallest.append(s + length - 1)
            
            # If the number of comparisons c is not within the range = [smallest, largest],
            # there is no array will sort with c comparisons.
            largest = l * (l - 1) // 2
            if c < smallest[l] or c > largest:
                result = '-1'
            else:
                # print(smallest[l])
                print(f'{count}: (l, c) = ({l}, {c})', end=', ')        
                sub_time0 = time()
                arr = rec(l, c, 1)
                sub_time1 = time()
                print(f'time = {sub_time1 - sub_time0:.3f} second')        
                # print(arr)
                # arr_sorted, result = lena_sort(arr)
            count += 1
            # print(result)
            # print(f'{result}, {c}')
        time1 = time()
        print(f'time = {time1 - time0:.3f} second')

