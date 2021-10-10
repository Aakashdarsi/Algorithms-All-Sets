import math
def factors(n):
    result = []
    for i in range(1,int(math.sqrt(n))):
        if n%i==0:
           if int(n/i)==i:
               result.append(i)
           else:
               result.append(i)
               result.append(int(n/i))
    print(result)

    

n = int(input())
factors(n)