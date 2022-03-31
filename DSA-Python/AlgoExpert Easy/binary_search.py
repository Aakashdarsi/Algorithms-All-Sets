# Recursive implementation 
def binary_search(array,target):
    return binary_search_helper(array,target,0,len(array)-1)

def binary_search_helper(array,targer,low,high):
    if low > high :
        return -1 
    middle = (low+high) // 2
    if array[middle] == targer:
        return middle 
    if array[middle] < targer:
        return binary_search(array,targer,middle+1,high)
    if array[middle] > targer:
        return binary_search(array,targer,low,middle-1) 

# Using iterative approach 

def binary_search_iterative(array,target):
    low = 0 
    high = len(array) - 1
    while low < high :
        mid = low + (high-low)//2
        if array[mid] == target :
            return mid 
        elif array[mid] < target :
            lwo = mid +1 

        else:
            high = mid -1 
    return -1