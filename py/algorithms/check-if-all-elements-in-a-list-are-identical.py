#coding:utf8
# 检查列表中所有元素是否相同

# input a list
# output
#   1. True if all elements in the input list evaluate as equal to each other using the standard equality operator
#   2. False otherwise


###########
# general method
def checkEqual1(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return true
    return all(first == rest for rest in iterator)

# one-liner
def checkEqual2(iterator):
    return len(set(iterator)) <= 1

# alse one-line
def checkEqual3(lst):
    return lst[1:] == lst[:-1]


########
# the simplest and most elegant way is as follows:
myList = [1, 2, 4, 9]
print all(x==myList[0] for x in myList)
# False


######
# http://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
