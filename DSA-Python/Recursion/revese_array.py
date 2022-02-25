# This method is using recursion 2 pointer method
# https://www.youtube.com/watch?v=twuC1F6gLI8&t=153s
def reverse(array,start,end):
    if start >end:
        return array
    if start < end:
        array[start],array[end] = array[end],array[start]
    return reverse(array,start+1,end-1)
array = list(map(int,input().split()))
x = reverse(array,0,len(array)-1)
print(x)