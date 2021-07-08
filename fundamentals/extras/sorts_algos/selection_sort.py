#selection sort
#sort in increasing order, starting by looking for the smallest #

def selection_sort(list):
    for i in range(0, len(list)-1, 1):
        currentMinimumIndex = i
        for j in range (i+1, len(list), 1):
            if(list[j] < list[currentMinimumIndex]):
                currentMinimumIndex = j
        if(currentMinimumIndex != i):
            list[i], list[currentMinimumIndex] = list[currentMinimumIndex], list[i]
    return list

someList = [2,8,5,1,2,7,9]
print(someList)
newList = selection_sort(someList)
print(newList)
