import time
from timeit import *

import numpy as np


def selection_sort(l):
    N = len(l)
    for i in range(N):
        # Find the minimum element in l[i:]
        min_index = i
        for j in range(i+1, N):
            if l[j] < l[min_index]:
                min_index = j
        # Exchange a[i] with smallest entry in a[i+1...N).
        l[i], l[min_index] = l[min_index], l[i]
    assert((l == sorted(l)).all())


def insertion_sort(l):
    N = len(l)
    for i in range(1,N):
        # insert l[i] in correct position of l[:i] (already sorted)
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
            else: break
    assert((l == sorted(l)).all())


def bubble_sort(l):
    N = len(l)
    for i in range(N):
        for j in range(N-1, i, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
    assert((l == sorted(l)).all())


def merge(l1, l2, l):
    n1 = len(l1)
    n2 = len(l2)
    i = i1 = i2 = 0
    while i1 < n1 and i2 < n2:
        if l1[i1] < l2[i2]:
            l[i] = l1[i1]
            i, i1 = i+1, i1+1
        elif l1[i1] > l2[i2]:
            l[i] = l2[i2]
            i, i2 = i+1, i2+1
        else:
            l[i], l[i+1] = l1[i1], l2[i2]
            i, i1, i2 = i+2, i1+1, i2+1
    while i1 < n1:
        l[i] = l1[i1]
        i, i1 = i+1, i1+1
    while i2 < n2:
        l[i] = l2[i2]
        i, i2 = i+1, i2+1
    return

def merge_sort(l):
    global aux
    N = len(l)
    if N == 1: return
    l1 = l[:N//2]    # NOTE: numpy slices 
    l2 = l[N//2:]    # are views not copies
    merge_sort(l1)
    merge_sort(l2)
    merge(l1, l2, aux)
    l[:] = aux[:N]
    assert((l == sorted(l)).all())    


if __name__ == '__main__':
    rng = np.random.default_rng()

    algorithms = (selection_sort, insertion_sort, bubble_sort, merge_sort,)
    sizes = (10, 25, 50, 75, 100, 200, 300, 400, 500)
    timing = np.empty((len(sizes), 1+len(algorithms)))
    aux = np.empty((max(sizes),))
    for i, N in enumerate(sizes):
        timing[i,0] = N
        for j, f in enumerate(algorithms):
            timing[i,j+1] = timeit(stmt="A = rng.uniform(-1e6, 1e6, N); f(A)", timer=time.process_time, number=100, globals=globals())

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    # repeat <x, y, optional style> 3-tuple as reqd. before kwargs
    plt.plot(timing[:,0], timing[:,1:5], label=[f.__name__ for f in algorithms])
    plt.legend()
    plt.show()

