def dig_produc(n):
    if n==0:
        return 1 
    else:
        return n%10 * dig_produc(n//10)
number = int(input())
result = dig_produc(number)
print(result)