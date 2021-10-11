def power(a,b):
    if b==0:
        return 1 
    else:
        result = power(a,b//2)
        if b&1 == 0:
            return (result*result)%10
        else:
            return (result*a*result)%10

number_of_test_cases = int(input())
for i in range(number_of_test_cases):
    a,b = list(map(int,input().split()))
    print(power(a,b))