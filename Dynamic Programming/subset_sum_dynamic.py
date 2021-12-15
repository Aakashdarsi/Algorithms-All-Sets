def subsetSum(a,sume,n):
    result = 0 
    if sume == 0:
        return True 
    elif n == 0:
        return False 
    if table[n][sume] != -1:
        return table[n][sume]
    
    if a[n-1]>sume:
        table[n][sume] = False
        

    else:
        result = subsetSum(a,sume,n-1) or subsetSum(a,sume-a[n-1],n-1)
        table[n][sume] = result
    return table[n][sume]




a = [1,2,3,4,5]
sume = 16
n = len(a)

table = [[-1 for i in range(sume+1)] for j in range(len(a)+1)]
res = subsetSum(a,sume,n)
print(res)