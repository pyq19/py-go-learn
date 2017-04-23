def insertion_sort(arr):
    for i in range(len(arr)):
        pre_index = i - 1
        current = arr[i]
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index+1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index+1] = current
    return arr

#if __name__ == '__main__':
#    l = [1, 2, 4, 3, 7, 6, 0]
#    print insertion_sort(l)


##########

def ins_sort(arr):
    for i in xrange(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > cursor:
            # swap the number down the list
            arr[pos] = arr[pos-1]
            pos = pos - 1
        # break and do the final swap
        arr[pos] = cursor
    return arr
