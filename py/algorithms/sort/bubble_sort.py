def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


##########
my_list = [12, 5, 8, 88, 66]
def bubble(l):
    length = len(l) - 1
    sorted= False
    while not sorted:
        sorted = True
        for i in range(length):
            if l[i] > l[i+1]:
                sorted = False
                l[i], l[i+1] = l[i+1], l[i]

bubble(my_list)
print my_list # [5, 8, 12, 66, 88]


##########
def bubble2(l):
    for passes_left in range(len(l)-1, 0, -1):
        for index in range(passes_left):
            if l[index] < l[index+1]:
                l[index], l[index+1] = l[index+1], l[index]
    return l
my_list = [12, 5, 8, 88, 66]
print bubble2(my_list) # [88, 66, 12, 8, 5]


###############
def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
my_list = [12, 5, 8, 88, 66]
print bubble_sort(my_list)#[5, 8, 12, 66, 88]


