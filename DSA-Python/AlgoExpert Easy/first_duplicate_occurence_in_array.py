# [1,2,3,1,4,5,6,7]
# https://www.youtube.com/watch?v=agrAZN4TBTA
# Here 1 is the first duplicate element 
# Approach 1
def duplicate_first(array):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                print(array[i],"is first duplicate")
                return 
    return "NO duplicates"

l = list(map(int,input().split(',')))
duplicate_first(l)