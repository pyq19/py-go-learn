arr = [5,4,3,1,6,8,10,9]

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print arr # [1, 3, 4, 5, 6, 8, 9, 10]
##################


for i in range(len(arr)):
    mini = min(arr[i:])         # find minimum element
    min_index = arr[i:].index(mini) # find index of minimum element
    arr[i + min_index] = arr[i]
    arr[i] = mini
print arr # [1, 3, 4, 5, 6, 8, 9, 10]
####################


def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
print selection_sort(arr)
###############


def se_sort(arr):
    for i in xrange(len(arr)):
        minimum = i
        for j in xrange(i+1, len(arr)):
            # "select" the correct value
            if arr[j] < arr[minimum]:
                minimum = j
        # using a pythonic swap
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr
print se_sort(arr)
