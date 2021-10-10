import math 
def prime_checker(i,a,n):
    count = 0 
    for number in range(2,i):
        if i%number==0:
            count+=1 
            break
    return count


n = int(input())
sqrt_num = int(math.sqrt(n))
a = []
for i in range(n+1):
    a.append(True)
for i in range(2,sqrt_num):
   x=  prime_checker(i,a,n)
   if x==0:
       for index in range(i+i,n+1,i):
           a[index]=False
for i in range(2,n+1):
    if a[i]==True:
        print(i)
