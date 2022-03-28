from numpy import arange


# https://www.youtube.com/watch?v=gf7vdIin0dk
# Method 1 Using extra space
def remove_duplicates_sorted_array(array):
    l = []
    for i in range(len(array)-1):
        if array[i] != array[i+1]:
            l.append(array[i])
    l.append(array[len(array)-1])
    print(l)
l = list(map(int,input().split()))
remove_duplicates_sorted_array(l)

# Method 2 Using constant space
def remove_duplicates_sorted_array(array):
    j = 0 
    for i in range(len(array)-1):
        if array[i] != array[i+1]:
            array[j] = array[i]
            j+= 1
    
    print(l)
l = list(map(int,input().split()))
remove_duplicates_sorted_array(l)
