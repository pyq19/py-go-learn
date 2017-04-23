#coding:utf8
# https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/5.mergeSort.md

def merge_sort(arr):
    import math
    if len(arr) < 2:
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

l = [1, 3, 2, 6, 5]

print merge_sort(l)
