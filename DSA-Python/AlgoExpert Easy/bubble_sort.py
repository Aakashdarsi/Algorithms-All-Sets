def bubble_sort(array):
    isSorted = False 
    counter = 0 
    while not isSorted:
        isSorted = True 
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                isSorted = False 
        counter += 1 
        
# Time Complexity is O(N^2)
# Space Complexity is O(1)