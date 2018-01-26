# -*- coding:utf-8 -*-

def binary_search(array, item):
    """二分查找,递归"""
    n = len(array)
    if n > 0:
        mid = n//2
        if array[mid] == item:
            return True
        elif item < array[mid]:
            return binary_search(array[:mid], item)
        else:
            return binary_search(array[mid+1:], item)
    return False
    
# 通用二分查找
def binary_search_2(array, item):
    """二分查找， 非递归"""
    n = len(array)
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high)//2
        guess = array[mid]# 检查中间的元素 
        if guess == item:# 找到元素
            return mid
        elif guess > item:# 数字大了
            high = mid - 1
        else:# 数字小了
            low = mid + 1
    return None

if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(li, 55))
    print(binary_search(li, 100))
    print(binary_search_2(li, 55))
    print(binary_search_2(li, 100))