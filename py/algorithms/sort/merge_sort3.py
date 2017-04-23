
def merge(left, right):
    '''
    takes two sorted sub lists and merges them in to a
    single sorted sub list and returns it

    :param left: a list of sorted integers
    :param right: a list of sorted integers
    :rtype: a list of sorted integers
    '''
    result = []
    n, m = 0, 0
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            result.append(left[n])
            n += 1
        else:
            result.append(right[m])
            m += 1
    
    result += left[n:]
    result += right[m:]
    return result

def sort(seq):
    '''
    takes a list of integers and sorts them in ascending order.
    this sorted list is then returned.

    :param seq: a list of integers
    :rtype: a list of sorted integers
    '''

    if len(seq) <= 1:
        return seq

    middle = int(len(seq) / 2)
    left = sort(seq[:middle])
    right = sort(seq[middle:])
    return merge(left, right)

print sort([1, 2, 5, 3, 8, 11, 4, 20, 2, 0])
# [0, 1, 2, 2, 3, 4, 5, 8, 11, 20]
