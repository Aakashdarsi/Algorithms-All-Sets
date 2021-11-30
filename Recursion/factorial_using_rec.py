def factorial(n):
    f = 1
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

f = int(input())
z = factorial(f)
print(z)