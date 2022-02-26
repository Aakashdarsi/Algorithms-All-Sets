def LCS_rec(string1,string2,n,m):
    if n == 0 or m == 0:
        return 0
    
    if string1[n-1] == string2[m-1]:
        return 1+LCS_rec(string1,string2,n-1,m-1)
    
    else:
        return max(LCS_rec(string1,string2,n-1,m),LCS_rec(string1,string2,n,m-1))


string1 = input()
string2 = input()
n = len(string1)
m = len(string2)
print(LCS_rec(string1,string2,n,m))