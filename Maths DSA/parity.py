def parity(n):
    count = 0 
    while n!=0:
        if n&1 ==1:
            count = count+1 
        n=n>>1
    return count


n = int(input())
result = parity(n) # if no of binary 1's are odd then parity is 1 else 0 
if result%2 ==0:
    print(0," is the parity")
else:
    print(1," is the paritt")