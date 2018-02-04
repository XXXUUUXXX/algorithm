# -*- coding: utf-8 -*-

# 快速排序
# 基本思想：通过一趟排序将要排序的数据分割成独立的两部分：分割点左边都是比它小的数，右边都是比它大的数
#     再按此方法对这两部分数据进行快速排序，整个排序过程都可递归进行
# 1.设置两个指针left和right，分别指向数组的头部和尾部，并以头部元素为基准值pivot
# 2.从右向左扫描，通过right指针，寻找比基准值小的元素，将其赋值给left指针所指位置
# 3.从左向右扫描，通过left指针，寻找比基准值大的元素，将其赋值给right指针所指位置
# 4.不断重复2,3步骤，直到left、right指针重合，将基准值赋值给重合位置，完成一次排序，然后递归进行排序
# 数据随机分布时，快速排序性能越好；数据越接近有序，快速排序性能越差
# 最优时间复杂度O(nlogn)
# 最坏时间复杂度O(n^2)
# 不稳定

def quick_sort(array, left, right):
    if left >= right: # 基线条件
        return
    low = left # low为序列左边的由左向右移动的游标
    high = right # high为序列右边的由右向左移动的游标
    pivot = array[low] # 设置头部元素为基准值
    while low < high:
        while low < high and array[high] > pivot: # high指向的元素比基准值大
            high -= 1
        array[low] = array[high]
        while low < high and array[low] <= pivot: # low指向的元素比基准值小
            low += 1
        array[high] = array[low]
    # 退出循环，low与high重合，都指向基准位置    
    array[low] = pivot # 将基准值放到该位置
    quick_sort(array, left, low - 1) #对基准值左边的子序列进行快速排序
    quick_sort(array, low + 1, right)

array = [54,26,93,17,77,31,44,55,20]
quick_sort(array,0,len(array)-1)
print(array)