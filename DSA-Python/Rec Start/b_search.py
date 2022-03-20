def b_search(arr,key,n,start):
    if start >= n:
        return "Key Not found"
    mid = (start+n)//2 
    if arr[mid] == key :
        return "found at index: "+str(mid)
    if arr[mid]>key:
        b_search(arr,key,mid-1,start)
    if arr[mid]<key:
        b_search(arr,key,n,mid+1)
    return "Not found"
    
    

    




arr = list(map(int,input().split()))
key = int(input())
n = len(arr)
print(b_search(arr,key,n-1,0))