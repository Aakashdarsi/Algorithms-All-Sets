def power(a,b):
    if b == 0 :
        return 1
    elif b == 1:
        return a
    else:
        final_ans = power(a, b//2)
        if b % 2 == 0:
            return final_ans * final_ans
        else:
            return final_ans * a * final_ans





a = int(input())
b = int(input())
result = power(a, b)
print(result)