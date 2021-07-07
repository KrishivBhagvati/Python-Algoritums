def quick_sort(sequnce):
    length = len(senqunce)
    if length <= 1:
    return sequnce
    else:
         pivot = sequence.pop()

         items_greater = []
         items_lower = []
         
         for items in seuence:
         if items > pivot:
            items_greaer.append(items)
          
         else:
              items_lower.append(items)

       return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([5, 6, 7, 9, 0, 6, 4, 3, 2]))