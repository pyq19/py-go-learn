def merge_sort(arr):
    # our recursive base case
    if len(arr) <= 1:
        return arr
    mid = len(arr) / 2
    # perform merge_sort recursively on both halves
    left, right = merge_sort(arr[mid:]), merge_sort(arr[:mid])
    # merge each side together
    return merge(left, right)

def merge(left, right):
    arr = []
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        # sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            arr.append(left[left_cursor])
            left_cursor += 1
        else:
            arr.append(right[right_cursor])
            right_cursor += 1
    # add the left overs if there's any left to the result 
    if left:
        arr.extend(left[left_cursor:])
    if right:
        arr.extend(right[right_cursor:])
    return arr

arr = [1,5, 7,4,3,2,1,9,0,10,43,64]
print(arr)
print(merge_sort(arr, 0, len(arr)-1))
#print merge_sort(arr)
print(arr)
