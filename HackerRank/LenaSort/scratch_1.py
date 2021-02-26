#!/usr/bin/python3.7

import math
import os
import random
import re
import sys

sys.setrecursionlimit(100000)



def search_biggest_sorted(length, comparisons):
    comparisons -= length - 1
 
    for less in range(length - 1):
        max_less = less * (less - 1) // 2
        comparisons_more = comparisons - max_less

        more = length - 1 - less
        max_more = more * (more - 1) // 2
        # print(f'\nless={less}')
        # print(f'\tcomparisons_more = {comparisons_more}')
        # print(f'\tmax_more = {max_more}')
        # print(f'\tmin_more = {smallest[more]}')
        if comparisons_more < smallest[more]:
            break
        
    less = less - 1
    comparisons_more -= less

    return less, comparisons_more


def foo(length, comparisons):
    while True:
        less, comparisons_more = search_biggest_sorted(length, comparisons)
        # pivot = less + 1
        more = length - 1 - less
        
        length, comparisons = more, comparisons_more
        print(f'length = {length}, comparisons = {comparisons}')
        input()

         
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

    length = 100000 
    comparisons = 475595761
    smallest = get_smallest(length)

    foo(length, comparisons)
    
