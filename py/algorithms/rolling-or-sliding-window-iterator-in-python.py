#coding:utf8
# http://stackoverflow.com/questions/6822725/rolling-or-sliding-window-iterator-in-python

# I need a rolling window (aka sliding window) iterable over a sequence/iterator/generator. 
# Default Python iteration can be considered a special case, where the window length is 1.

def rolling_window(seq, window_size):
    it = iter(seq)
    win = [it.next() for cnt in xrange(window_size)]    # first window
    yield win
    for e in it:        # subsequent window
        win[:-1] = win[1:]
        win[-1] = e
        yield win
# if __name__ == '__main__':
#     for w in rolling_window(xrange(6), 3):
#         print w
# [0, 1, 2]
# [1, 2, 3]
# [2, 3, 4]
# [3, 4, 5]


############
# there's one in an old version of the Python docs with itertools examples.
# https://docs.python.org/release/2.3.5/lib/itertools-example.html

from itertools import islice
def window(seq, n=2):
    'returns a sliding window (of width n) over data from the iterable'
    ' s -> (s0, s1, ... s[n-1]), (s1, s2, .. ,sn)...'
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result
# The one from the docs is a little more succinct and uses itertools to greater effect I imagine.

for w in window(xrange(6), 3):
    print w
# (0, 1, 2)
# (1, 2, 3)
# (2, 3, 4)
# (3, 4, 5)


###############
from itertools import tee, izip
def window2(iterable, size):
    iters = tee(iterable, size)
    for i in xrange(1, size):
        for each in iters[i:]:
            next(each, None)
    return izip(*iters)
for each in window2(xrange(6), 3):
    print list(each)
#[0, 1, 2]
#[1, 2, 3]
#[2, 3, 4]
#[3, 4, 5]
