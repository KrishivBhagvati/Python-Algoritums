def bubble(list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
    sorted = True
    for i in range(0, indexing length):
        if list_a[i] > list_a[i+1]:
           sorted = False
           list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
return list_a

print(bubble([2,3,5,7,6,9,8,0]))