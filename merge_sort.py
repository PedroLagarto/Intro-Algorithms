import numpy as np
import pytest
import math  

A = [7, 4, 6, 10, 2, 5, 3, 13, 7, 9, 10, 50, 2, 3, 6 ,1, 2,3,7,5,8,0,2,2,2,2,5,5,7,8,9,10]

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

B = merge_sort(A)
print(B)
