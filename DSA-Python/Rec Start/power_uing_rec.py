def power(n,p,c):
    if c == 0:
        return 1 
    return n*power(n,p,c-1)




n = int(input())
p = int(input())
count = p
print(power(n,p,count))