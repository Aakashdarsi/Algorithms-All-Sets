# Parameterised way of recursion
# parameters are affected while applying recursion 

def fact(num,facto):
    if num <=1:
        print(facto)
        return 
    fact(num-1,facto*num)
    

n = int(input())

fact(n,1)
