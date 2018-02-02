# -*- coding:utf-8 -*-

# 冒泡排序是一种交换排序。两两比较待排序的关键字，并交换不满足次序要求的那对数，直到整个表都满足次序要求为止。
# 假设有一个大小为N的无序序列，以升序冒牌排序为例，每次排序过程中通过两两比较相邻元素，将小的数字放到前面，大的数字放在后面。
# 冒泡排序把小的元素往前调或大的元素往后调，相同元素的前后顺序没有改变
# 冒泡排序是一种稳定排序算法

array = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
n = len(array)

def bubble_sort(array):
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                count += 1
        if 0 == count:
            return array
#-------------------------------------------------------------------------------
def bubble_sort2(array):
    flag = 1
    for j in range(n-1,0,-1):
        if flag:
            flag = 0
            for i in range(j):
                if array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]
                    flag = 1
        else:
            break
    return array
#-------------------------------------------------------------------------------
def bubble_sort3(array):
    if n == 0:
        return []
    for j in range(n - 1):
        bChanged = False
        for i in range(n - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                bChanged = True
        if not bChanged:
            break
    return array


b = bubble_sort3(array)
print(b)