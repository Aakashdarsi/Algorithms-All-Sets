def palindrome(string,start,n):
    if start >= n//2:
        return True 
    if string[start] != string[n-start-1]:
        return False 
    return palindrome(string,start+1,n)

string = input()
res = palindrome(string,0,len(string))
print(res)