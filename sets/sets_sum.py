array = [5, 7, 2, 3, 1, 0]
checked_set = set([])

for i in range(len(array)):
    num = array[i]
    complement = 7 - num
    checked_set.add(complement)
    
    if num in checked_set:
        print(num, complement)