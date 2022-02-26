def sum_of_subsets(set_ele,sum_to,n):
    if sum_to == 0:
        return True
    if sum_to !=0 and n == 0:
        return False
    if set_ele[n-1] > sum_to:
        return sum_of_subsets(set_ele,sum_to,n-1)
    else:
        return sum_of_subsets(set_ele,sum_to,n-1) or sum_of_subsets(set_ele,sum_to-set_ele[n-1],n-1)






set_ele = list(map(int,input().split()))
sum_to = int(input())
n = len(set_ele)
print(sum_of_subsets(set_ele,sum_to,n))