def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)
    
    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min-value = j

         if min_value != 1: 
            list_a[min_value], list[i] = list[a], list_a[min_value]

     return list_a
     
      print(selection_sort([3,4,35,6,78,,9]))
      
