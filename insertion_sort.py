import numpy as np
import pytest

A = [7, 4, 6, 10, 2, 5, 3, 13, 7, 9]


def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

print (insertion_sort(A))


