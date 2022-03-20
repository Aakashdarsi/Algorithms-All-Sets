# Important to remember this logic VVIMP!!!

def subseq(s,start,end,arr):
    if start >= end :
        print(arr)
        return
    
    subseq(s,start+1,end,arr)
    arr.append(s[start])
    subseq(s,start+1,end,arr)
    arr.pop()

    


s = input()
n = len(s)
arr = []
subseq(s,0,n,arr)