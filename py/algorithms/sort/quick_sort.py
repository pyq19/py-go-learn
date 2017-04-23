#coding:utf8

# pivot 支点，中心

def quick_sort(lists, left, right):
    pass

def sort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sort(less) + sort(equal) + sort(greater)
    else:
        return arr

ar = [12,4,5,6,7,3,1,15]
print sort(ar) # [1, 3, 4, 5, 6, 7, 12, 15]

def qsort(arr):
    pivind = 0
    l, r, pivot = [], [], []
    for x in arr:
        if arr[pivind] == x: 
            pivot.append(x)
        elif arr[pivind] > x:
            l.append(x)
        else:
            r.append(x)
    if len(l) > 1:
        l = qsort(l)
    if len(r) > 1:
        r = qsort(r)
    return (l + pivot + r)

print qsort(ar) # [1, 3, 4, 5, 6, 7, 12, 15]
