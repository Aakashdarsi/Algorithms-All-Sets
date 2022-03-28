def selection_sort(array):
    currIndex = 0
    while currIndex < len(array) -1:
        smallestIndex = currIndex
        for i in range(currIndex,len(array)):
            if array[smallestIndex] > array[i]:
                smallestIndex= i 
        array[currIndex],array[smallestIndex] = array[smallestIndex],array[currIndex]
        currIndex += 1
l = list(map(int,input().split()))
selection_sort(l)
print(l)