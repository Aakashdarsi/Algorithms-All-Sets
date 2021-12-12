def count(n):
    no_of = 0
    if n == 0:
        no_of +=1 
    else:
        last_dig =  n%10 
        if last_dig == 0:
            no_of+=1 
        count(n//10)
    return no_of
     
n = int(input())
result = count(n)
print(result)