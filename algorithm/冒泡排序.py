# -*- coding:utf-8 -*-
def d_sort(arr):
    n = len(arr)
    for i in range(n):

        swapped = False

        #正序实现
        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

                swapped = True

        if not swapped:
            break


arr = [12,24,23,78,22,45]

d_sort(arr)

print(arr)

print(list(range(2,0,-1)))



'''
        #逆序实现
        for j in range(n-1,i,-1):
            if arr[j] > arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]

            swapped = True
'''
