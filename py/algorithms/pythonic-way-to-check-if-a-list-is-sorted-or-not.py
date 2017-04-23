# is there a pythonic way to check if a list is already sorted in ASC or DESC
listtimestamps = [1, 2, 3, 5, 6, 7]
# something like isttimestamps.isSorted() that returns True or False.
# I want to input a list of timestamps for some messages and check if the the transactions appeared in the correct order.


##########
l = listtimestamps 
print all(l[i] <= l[i+1] for i in xrange(len(l)-1)) # True


###########
def is_sorted(l):
    return all(a <= b for a, b in zip(l[:-1], l[1:]))


###########
from itertools import imap, tee
import operator

def is_sorted2(iterable, compare=operator.le):
    a, b = tee(iterable)
    next(b, None)
    return all(imap(compare, a, b))
    

if __name__ == '__main__':
    print is_sorted(l)
    print is_sorted2(l)
