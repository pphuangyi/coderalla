#!/usr/bin/python3.7

import math
import os
import random
import re
import sys

sys.setrecursionlimit(100000)


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
    

def foo(less, length, comparisons):
    more = length - 1 - less
    max_more, min_more = more * (more - 1) // 2, smallest[more]
    max_less, min_less = less * (less - 1) // 2, smallest[less]
        
    lower = max(min_less, comparisons - max_more)
    upper = min(max_less, comparisons - min_more)
    
    return upper >= lower


def search(length, comparisons):
    f, t = 0, (length + 1) // 2
    while f < t:
        middle = (f + t) // 2
        if foo(middle, length, comparisons):
            t = middle
        else:
            f = middle + 1
    return f
 

def rec(length, comparisons, first):

    if length == 0:
        return []
    if length == 1:
        return [first]
    
    comparisons -= length - 1

    less = search(length, comparisons)
    more = length - 1 - less

    max_more, min_more = more * (more - 1) // 2, smallest[more]
    max_less, min_less = less * (less - 1) // 2, smallest[less]
    lower = max(min_less, comparisons - max_more)
    upper = min(max_less, comparisons - min_more)
    
    pivot = first + less
    # print(f'less = {less}, more = {more}')
    # print(f'less half: ({min_less}, {max_less})')
    # print(f'more half: ({min_more}, {max_more})')
    # print(f'(lower, upper) = ({lower}, {upper})')
    if lower == comparisons - max_more:     # comparisons_more = max_more
        comparisons_less = lower        
        A = rec(less, comparisons_less, first)
        B = list(range(pivot + 1, pivot + 1 + more))
    elif upper == comparisons - min_more:   # comparisons_more = min_more
        comparisons_less = upper        
        A = rec(less, comparisons_less, first)
        B = get_min_arr(more, pivot + 1)
    else: # upper == max_less
        comparisons_less = upper
        comparisons_more = comparisons - comparisons_less
        A = list(range(first, first + less))
        B = rec(more, comparisons_more, pivot + 1)

    return [pivot] + A + B


def get_smallest(length):
    smallest = [0, 0]
    for l in range(len(smallest), length + 1):
        s = smallest[(l - 1) // 2] + smallest[l // 2] + l - 1
        smallest.append(s)
    return smallest


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

        
if __name__ == '__main__':
    

    length = int(sys.argv[1])
    arr = list(range(1, length + 1))
    random.shuffle(arr)
    
    arr_sorted, comparisons = lena_sort(arr)
    # print(f'arr = {arr}')
    print(f'comparisons = {comparisons}')

    smallest = get_smallest(length)
    # print(smallest)
    brr = rec(length, comparisons, 1)
    
    brr_sorted, comparisons = lena_sort(brr)
    # print(f'sorted array = {brr_sorted}')
    print(f'comparisons = {comparisons}')


    
