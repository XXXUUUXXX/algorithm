# -*- coding:utf-8 -*-

# 时间复杂度O(n²)
# 选择排序：每趟从待排序的记录中选出关键字最小的记录，顺序放在已排序的记录序列末尾，直到全部排序结束为止
# 1.从待排序序列中找到关键字最小的元素
# 2.如果最小元素不是待排序序列的第一个元素，将其和第一个元素互换
# 3.从余下的N-1个元素中，找出关键字最小的元素，重复第1,2步，直到排序结束
# 选择排序的比较次数和序列的初始排序无关，假设待排序的序列有N个元素，则比较次数总是N(N-1)/2
# 移动次数与序列的初始排序有关。当序列为正序时，移动次数为0，反序时，移动次数为3N(N-1)/2
def selection_sort(array):
    n = len(array)
    if n == 0:
        return []
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
