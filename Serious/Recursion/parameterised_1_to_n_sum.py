#https://www.youtube.com/watch?v=69ZCDFy-OUo&t=212s
def sum_i(n,sum):
    if n<1:
        print(sum)
        return
    sum_i(n-1,sum+n)
    


n= int(input())
sum_i(n,0)