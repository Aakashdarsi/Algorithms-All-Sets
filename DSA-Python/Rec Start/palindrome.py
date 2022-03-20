def palindrome(string,start,end):
    if start >end:
        return True
    if string[start] != string[end]:
        return False
    else:
        return palindrome(string,start+1,end-1)

    


string = input()
res = palindrome(string,0,len(string)-1)
if res == True:
    print("Pal")
else:
    print("not")
