
def search(seq, key):
    '''
    takes a list of integers and searches if the `key` is contained within
    the list.

    :param seq: a list of integers
    :param key: the integer to be searched for
    :rtype: the index of where the `key` is located in the list.
            if `key` is not found then False is returned.
    '''
    lo = 0
    hi = len(seq) - 1
    while hi >= lo:
        mid = lo + (hi - lo) // 2
        if seq[mid] < key:
            lo = mid + 1
        elif seq[mid] > key:
            hi = mid - 1
        else:
            return mid
    return False

# print search([1,2,3,4,5], 3) # 2

l = [100, 200, 300, 400, 500]
print 'list ->', l
print 'the index of 200 in l is ->', search(l, 200)

