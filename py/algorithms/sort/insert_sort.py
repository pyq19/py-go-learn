def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

def ins_sort(k):
    for i in range(1, len(k)):
        j = i
        while j > 0 and k[j] < k[j-1]:
            k[j], k[j-1] = k[j-1], k[j]
            j = j - 1
    return k

ll = [1, 4, 2, 3, 8, 5]

print ins_sort(ll)
print insert_sort(ll)
# [1, 2, 3, 4, 5, 8]
