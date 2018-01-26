# -*- coding:utf-8 -*-

# 时间复杂度O(n²)


def selection_sort(array):
    n = len(array)
    # 需要进行n-1次选择操作
    for i in range(n-1):
        # 记录最小位置
        min_index = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
array = [54,226,93,17,77,31,44,55,20]
selection_sort(array)
print(array)

#-------------------------------------------------------------------------------

def findsmallest(array):
    smallest = array[0] # 存储最小的值
    smallest_index = 0 # 存储最小元素的索引
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selectionSort(array):
    new_array = []
    for i in range(len(array)):
        smallest = findsmallest(array) # 找出数组总最小的元素，并将其加到新数组中
        new_array.append(array.pop(smallest))
    return new_array
print selectionSort([5, 3, 6, 2, 10])