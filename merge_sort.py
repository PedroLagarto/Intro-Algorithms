import numpy as np
import pytest
import math  

A = [7, 4, 6, 10, 2, 5, 3, 13, 7, 9, 10, 50, 2, 3, 6]

def merge_sort(A,s,e):
    if s < e:
        m = (s+e) // 2
        merge_sort(A,s,m)
        merge_sort(A,m+1,e)
        merge(A,s,m,e)
    else: 
        return A[s:e+1]

def merge(A,s,m,e):
    left = A[s:m]
    right = A[m+1:e+1]
    i = 0
    j = 0
    k = 0
    B = []
    while i != len(left) or j != len(right):
        if left[i] >= right[j]:
            B[k] = left[i]
            i = i + 1
            k = k + 1
        else:
            B[k] = right[j]
            j = j + 1
            k = k + 1
    return B

merge_sort(A,0,15)