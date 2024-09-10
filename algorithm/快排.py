# -*- coding:utf-8 -*-
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# 示例使用：
example_list = [3, 6, 8, 10, 1, 2, 1, 4, 7, 5]
sorted_list = quicksort(example_list)
print(sorted_list)  # 输出: [1, 1, 2, 3, 4, 5, 6, 7, 8, 10]
