# ith largest element is placed at end of that array meaning tothe right side of the array 
def bubble_sort(array,n):
    if n == 0 or n ==1:
      
        return 
    
    for i in range(n-1):
        if array[i]>array[i+1]:
            array[i],array[i+1]= array[i+1],array[i]
    bubble_sort(array,n-1)
array = list(map(int,input().split()))
bubble_sort(array,len(array))
print(array)
