def palindrome(n):
    if n == 0:
        return 
    reverse = 0 
    rem = n%10 
    reverse = reverse*10+ rem 
    palindrome(n//10)
    


n = int(input())
x = palindrome(n)