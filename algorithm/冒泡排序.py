# -*- coding:utf-8 -*-
def d_sort(arr):
    n = len(arr)
    for i in range(n):

        swapped = False

        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

                swapped = True

        if not swapped:
            break


arr = [12,24,23,78,22,45]

d_sort(arr)

print(arr)
