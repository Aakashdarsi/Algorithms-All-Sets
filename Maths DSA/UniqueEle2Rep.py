n = list(map(int,input().split()))
result = 0 
for i in n:
    result= result^i
print(result)