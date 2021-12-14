num = int(input())
array = [0 for i in range(num+1)]
array[1] = 1 
for i in range(2,num+1):
    array[i] = i*array[i-1]
print(array[num])
