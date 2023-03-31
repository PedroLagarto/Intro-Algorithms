import numpy as np
import random
import time



def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

for n in [10, 100, 1000, 10000]:
    A = random.sample(range(1,n+1), n)
    print("=================")
    # print("Before sorting")
    # print(A)
    start = time.time()
    sortedA = insertion_sort(A)
    end = time.time()
    elapsed_time = end - start
    # print("After sorting")
    # print(sortedA)
    print(f"n = {n}, elapsed_time = {elapsed_time}")




