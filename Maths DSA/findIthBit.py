n = int(input())
i = int(input())
mask = 1<<i 
if n&i !=0:
    print(1," is present at that position")
else:
    print("Zero is present at that position")