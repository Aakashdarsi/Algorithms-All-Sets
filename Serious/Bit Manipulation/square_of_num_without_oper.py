#https://www.geeksforgeeks.org/calculate-square-of-a-number-without-using-and-pow/
#https://www.youtube.com/watch?v=pOKuLSKnAW4
n = int(input())
if n <0:
    n = -n 
temp = n 
count = 0 
res = 0 
while temp !=0 :
    if temp&1 ==1:
        res+=n<<count 
    count +=1 
    temp = temp>>1
