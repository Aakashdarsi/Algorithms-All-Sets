def power(a,b):
    if b==0:
        return 1 
    else:
        result = power(a,b//2)
        if b&1 == 0:
            return (result*result)
        else:
            return (result*a*result)

number_of_test_cases = int(input())
for i in range(number_of_test_cases):
    a,b = list(map(int,input().split()))
    r = power(a,b)
    convert_string = str(r)
    first_three = convert_string[:3]
    last_three = convert_string[-3:]
    final_res = first_three+"..."+last_three
    print(final_res)