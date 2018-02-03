# -*- coding:utf-8 -*-

# 插入排序
# 通过构建有序序列，对于为排序的数据，在已经排序的序列中从后向前扫描，找到相应位置并插入
# 在从后往前扫描过程中，需要反复把已排序元素逐步往后挪位，为最新元素提供插入空间
# 插入排序是一种稳定排序算法
# 正序时，最优时间复杂度O(n)
# 反序时，最坏时间复杂度O(n^2)
# 数据越接近正序，直接插入排序的算法性能越好

def insert_sort(array):
    if len(array) == 0:
        return []
    for i in range(1, len(array)):
        for j in range(i,0,-1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array
#-------------------------------------------------------------------------------
def insert_sort2(array):
    if len(array) == 0:
        return []
    for i in range(1, len(array)):
        j = i
        while j > 0:
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                j -= 1
            else:
                break
    return array
    
array = [6, 4, 8, 9, 2, 3, 1]
print(insert_sort2(array))