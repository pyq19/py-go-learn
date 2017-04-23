
def sort(seq):
    '''
    Takes a list of integers and sorts them in ascending order.
    This sorted list is then returned.

    :param seq: A list of integers
    :rtype: A list of sorted integers
    '''

    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left, right = [], []
        for x in seq[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return sort(left) + [pivot] + sort(right)

if __name__ == '__main__':
    l = [1, 5, 2, -10, 100, 20, 3]
    print l
    print sort(l)
# [1, 5, 2, -10, 100, 20, 3]
# [-10, 1, 2, 3, 5, 20, 100]
