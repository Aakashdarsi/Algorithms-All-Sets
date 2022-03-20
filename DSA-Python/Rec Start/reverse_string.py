def reverse(str,start,end):
    if start>end:
        print("".join(str))
        return 
    str[start],str[end] = str[end],str[start]
    reverse(str,start+1,end-1)

str = list(input())

reverse(str,0,len(str)-1)