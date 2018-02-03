# -*- coding:utf-8 -*-

# 希尔排序又称为缩小增量排序，是一种加强版的插入排序
# 希尔排序是不稳定排序算法
"""
{13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10}
以步长为5进行排序
10 14 73 25 23
13 27 94 33 39
25 59 94 65 82
45
以步长为3进行排序
10 14 73
25 23 13
27 94 33
39 25 59
94 65 82
45
最后以步长为1变为插入排序
"""
# 步长<=>列数
# 最优时间复杂度：根据步长序列的不同而不同
# 最坏时间复杂度：O(n^2)

# 以步长为n/2为例
def shell_sort(array):
    n = len(array)
    if n == 0:
        return []
    gap = n // 2
    while gap > 0:
        for i in range(gap,n):
            j = i
            while j > 0:
                if array[j] < array[j-gap]:
                    array[j], array[j-gap] = array[j-gap], array[j]
                    j -= gap
                else:
                    break
        gap //= 2
    return array

array = [6, 4, 8, 9, 2, 3, 1]
print(shell_sort(array))