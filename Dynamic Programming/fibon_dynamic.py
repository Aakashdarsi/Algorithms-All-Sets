n = int(input())
array = []
for i in range(n+1):
    array.append(0)
array[1] = 1 
for i in range(2,n+1):
    array[i] = array[i-1]+array[i-2]
print(array[n])