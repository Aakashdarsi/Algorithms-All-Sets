def reverse_digits(n):
    reverse = 0
    if n==0:
        return 
    rem = n%10 
    reverse*=10+rem
    reverse_digits(n//10)
   
        
        
    

n = int(input())
result = reverse_digits(n)
print(result)