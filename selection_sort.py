# -*- coding:utf-8 -*-
def selection_sort(alist):
    n = len(alist)
    # 需要进行n-1次选择操作
    for i in range(n-1):
        # 记录最小位置
        min_index = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]
alist = [54,226,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)

#-------------------------------------------------------------------------------

def findsmallest(alist):
    smallest = alist[0] # 存储最小的值
    smallest_index = 0 # 存储最小元素的索引
    for i in range(1, len(alist)):
        if alist[i] < smallest:
            smallest = alist[i]
            smallest_index = i
    return smallest_index

def selectionSort(alist):
    new_alist = []
    for i in range(len(alist)):
        smallest = findsmallest(alist) # 找出数组总最小的元素，并将其加到新数组中
        new_alist.append(alist.pop(smallest))
    return new_alist
print selectionSort([5, 3, 6, 2, 10])