# reverse an array using recursion 
def reverse(array,start,end):
    if start >= end :
        print(array)
        return 
    
    array[start] ,array[end] = array[end],array[start]
    reverse(array,start+1,end-1)
    
        
array = list(map(int,input().split()))
l = 0 
end = len(array)-1
reverse(array,l,end)