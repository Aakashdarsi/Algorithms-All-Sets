# functional way of recursion


def fact(num):
    if num <=1:
       return 1
    return num*fact(num-1) 
    # f(3) we are computing
    # 1st rec = 3*f(2) 3 will wait for f(2)
    # 2 nd rec = 3*2*f(1) will wait for f(1)
    # 3 rec = 3*2*1 recursion completed as there are no function calls
    # it returns
    
    

n = int(input())

print(fact(n))