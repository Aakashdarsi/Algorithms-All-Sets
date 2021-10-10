def factors(n):
    factors = ""
    for i in range(1,n):
        if n%i==0:
            factors+=str(i)+" "
    return factors



n = int(input())
result = factors(n)
print(result)