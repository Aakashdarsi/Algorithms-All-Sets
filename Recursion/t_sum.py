def digit(n):
    if n ==0:
        return 0 
    else:
        return n%10 + digit(int(n/10)) 



n = int(input())
y = digit(n)
print(y)