import math
def primechecker(number):
    t = False
    for i in range(2,number):
        if number%i==0:
            t = True
            break
    if t==True:
        print(str(number)+" is not a prime")
    else:
        print(str(number)+" is a prime")
    


n = int(input())
final = False
for i in range(2,n):
    primechecker(i)



