def sqrt(n,precison):
    low = 0 
    high = n - 1
    result = 0 
    while low<=high:
        mid = (low+high)//2
        if mid*mid<=n:
            result = mid
            low=mid+1  
        elif mid*mid>n:
            high = mid-1
    if result!=0:
        increment_value = 0.1
        while precison!=0:
            while result*result<=n:
                result = result+increment_value
            result = result - increment_value
            increment_value/=10
            precison-=1
        print(round(result,precison))
    
                
             
    




n = int(input("Enter the value: "))
precison = int(input("Enter the Preciosn upto: "))
sqrt(n,precison)