"""
Student Naam:   Wouter Dijkstra
Student Nr. :   1700101
Klas        :   ??
Docent      :   frits.dannenberg@hu.nl
"""

import random


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def generate_list(n):
    random_list = []

    for x in range(n):
        random_list.append(random.randint(0, 100))

    return random_list


def qsort(a, low=0, high=-1):
    x = 0
    if high == -1:
        high = len(a) - 1
    if low < high:
        swap(a, low, random.randint(low, high))
        m = low
        for j in range(low + 1, high+1):
            if a[j] < a[low]:
                m += 1
                swap(a, m, j)
            x += 1
        swap(a, low, m)
        if m > 0:
            qsort(a, low, m - 1)
        qsort(a, m + 1, high)

array = generate_list(100)
qsort(array, 0, 99)
print(array)
