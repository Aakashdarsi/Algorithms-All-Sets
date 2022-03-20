dest = int(input())
dest_arr = [0 for i in range(dest+1)]
dest_arr[-1] = 1 
dest_arr[-2] = 1 
for i in range(dest-2,-1,-1):
    dest_arr[i] = dest_arr[i+1]+dest_arr[i+2]
print(dest_arr)
print("Total number of ways to reach the destination ")
print(dest_arr[0])