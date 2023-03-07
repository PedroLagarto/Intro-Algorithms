import numpy as np
import pytest
import math  

A = [7, 4, 6, 10, 2, 5, 3, 13, 7, 9, 10, 50, 2, 3, 6]

def merge_sort(A,s,e):
    if e-s <= 1:
        return A[s:e+1]
    m = (s+e) // 2
    merge_sort(A,s,m)
    merge_sort(A,m,e)
    merge(A,s,m,e)
    return A


def merge(A,s,m,e):
    left = A[s:m]
    right = A[m:e]
    i = 0
    j = 0
    B = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
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

B = merge_sort(A,0,15)
print(B)
