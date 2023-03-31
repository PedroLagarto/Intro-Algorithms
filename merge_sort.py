import numpy as np
import pytest
import math
import time  
import random


def merge_sort(A):
    size = len(A)
    if size == 1:
        return A
    else:
        m = size // 2
        left = A[:m]
        right = A[m:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left,right)

def merge(left, right):
    i = 0
    j = 0
    B = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            B.append(left[i])
            i = i + 1
        else:
            B.append(right[j])
            j = j + 1
    
    while i < len(left):
        B.append(left[i])
        i = i + 1

    while j < len(right):
        B.append(right[j])
        j = j + 1
    return B



for n in [10, 100, 1000, 10000]:
    A = random.sample(range(1,10*n), n)
    print("=================")
    # print("Before sorting")
    # print(A)
    start = time.time()
    sortedA = merge_sort(A)
    end = time.time()
    elapsed_time = end - start
    print("After sorting")
    print(sortedA)
    print(f"n = {n}, elapsed_time = {elapsed_time}")


