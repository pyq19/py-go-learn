def quick_sort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partition_index = partition(arr, left, right)
        quick_sort(arr, left, partition_index-1)
        quick_sort(arr, partition_index+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


####################

def quick_sort(arr, first, last):
    if first < last:
        pos = partition(arr, first, last)
        print arr[first:pos-1], '====', arr[pos+1:last]
        # start our two recursive calls
        quick_sort(arr, first, pos-1)
        quick_sort(arr, pos+1, last)

def partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]: # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
#    print wall
    return wall

arr = [1,5,65,23,57,1232,-1,-5,-2,242,100,4,423,2,564,9,0,10,43,64]
print arr
quick_sort(arr, 0, len(arr)-1)
print arr
