def l_search(arr,start,n,key):
    if start >= n:
        print(str(key)+" Not found")
        return 
    if arr[start] == key :
        print("Key found at : "+str(start))
        return 

    l_search(arr,start+1,n,key)




arr = list(map(int,input().split()))
key = int(input())
l_search(arr,0,len(arr),key)