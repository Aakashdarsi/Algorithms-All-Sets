
def tryRes(number):
    sum_el = 0 
    pr = 1
    while number!=0:
        digit = number%10 
        sum_el+=digit
        pr = pr*digit
        number//=10
    return pr-sum_el


n = int(input())
result = tryRes(n)
print(result)