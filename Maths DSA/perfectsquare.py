def findper(n):
    low = 0 
    high = n - 1
    result = 0 
    while low<=high:
        mid = (low+high)//2
        if mid*mid==n:
            result = mid
            return result
        elif mid*mid<n:
            low = mid+1 
        elif mid*mid>n:
            high = mid - 1 
    return result

n = int(input())
print(findper(n))