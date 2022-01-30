#https://www.youtube.com/watch?v=69ZCDFy-OUo&t=212s
def sum_i(n,sum):
    if n<1:
        print(sum) # Here sum is a parameter so we are returning a parameter so it's a parameterised recusion returning a paramerter
        return
    sum_i(n-1,sum+n)
    


n= int(input())
sum_i(n,0)