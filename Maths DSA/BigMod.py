def power(a,b,c):
    if b==0:
        return 1 
    else:
        result = power(a,b//2,c)
        if b&1 == 0:
            return (result*result)%c
        else:
            return (result*a*result)%c

a = int(input())
b = int(input())
c = int(input())
print(power(a,b,c))