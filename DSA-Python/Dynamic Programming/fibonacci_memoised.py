n = int(input())
array = [-1 for i in range(n+1)]
array[0] = 0 
array[1] = 1 
for i in range(2,n+1):
    array[i] = array[i-1]+array[i-2]
print(array[n]) # Memoisation is process of storing already computed problme so that wheneveer we encounter we can directly retun the value without solving it
