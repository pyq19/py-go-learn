#coding:utf8
'''
    Insertion Sort
    --------------
    A sort that uses the insertion of elements in to the list to sort the list.

    Time Complexity: O(n**2)

    Space Complexity: O(n) total
'''

def sort(seq):
    '''
    Takes a list of integers and sorts them in ascending order.
    This sorted list is then returned.

    :param seq: A list of integers
    :rtype: A list of integers
    '''
    for n in range(1, len(seq)):
        item = seq[n]
        hole = n
        while hole > 0 and seq[hole-1] > item:
            seq[hole] = seq[hole-1]
            hole = hole - 1
        seq[hole] = item
    return seq


def ins_sort(k):
    for i in range(1, len(k)):
        j = i
        while j > 0 and k[j] < k[j-1]:
            k[j], k[j-1] = k[j-1], k[j]
            j = j - 1
    return k
    
if __name__ == '__main__':
    l = [1, 3, -2, 5, 2, 100, 9]
    print l
    print sort(l)
    print ins_sort(l)

# [1, 3, -2, 5, 2, 100, 9]
# [-2, 1, 2, 3, 5, 9, 100]
# [-2, 1, 2, 3, 5, 9, 100]
