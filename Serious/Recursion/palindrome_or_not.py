from heapq import nsmallest
from re import S


def palindrome(n,start,end):
    if start >= (end+1)//2:
        return True
    if n[start] != n[end-start]:
        return False 
    return palindrome(n,start+1,end)
         


n = input()
palindrome(n,0,len(n-1))