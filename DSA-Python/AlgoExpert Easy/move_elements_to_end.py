# Time complexity O(1)
def move_elements_to_end(array,value):
    i = 0 
    j = len(array) -1 
    while i < j :
        while array[j] == value :
            j -= 1
        if array[i] == value :
             array[i],array[j] = array[j],array[i]
        i += 1 
    return array 

l = list(map(int,input().split()))
target = int(input())
print(move_elements_to_end(l,target))