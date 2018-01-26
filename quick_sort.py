# -*- coding: utf-8 -*-

# 快速排序
# 1.从数组中选择一个元素，这个元素被称为基准值(pivot)
# 2.将数组分成两个子数组：小于基准值的元素和大于基准值的元素
# 3.对这两个子数组进行快速排序
# 时间复杂度O(nlogn)

def quick_sort(array, left, right):
    if left >= right: # 基线条件
        return
    low = left # low为序列左边的由左向右移动的游标
    high = right # high为序列右边的由右向左移动的游标
    pivot = array[low] # 设置基准值
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
#-------------------------------------------------------------------------------

# 算法图例
def quicksort(array):
    if len(array) < 2:
        return array # 基线条件
    else:
        pivot = array[0] # 递归条件
        less = [i for i in array[1:] if i <= pivot] # 由所有小于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i < pivot] # 由所有大于基准值的元素组成的子数组
        return quicksort(less) + pivot + quictsort(greater)
