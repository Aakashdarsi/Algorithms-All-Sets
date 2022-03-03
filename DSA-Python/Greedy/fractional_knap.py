# https://www.sanfoundry.com/python-program-solve-fractional-knapsack-problem-using-greedy-algorithm/
# Greedy Knapsack
def grknap(weights,profits,bag_weight,n):
    index_array = list(range(n))
    v_w_ratio_arr = [p/w for p,w in zip(profits,weights)]
    index_array.sort(key = lambda x : v_w_ratio_arr[x],reverse = True)
    max_profit = 0
    fractions_to_be_taken = [0] * n
    for i in index_array:
        if weights[i] <= bag_weight:
            fractions_to_be_taken[i] = 1 
            bag_weight -= weights[i]
            max_profit += profits[i]
        else:
            fractions_to_be_taken[i] = bag_weight/weights[i]
            max_profit += profits[i]*fractions_to_be_taken[i]
            break
    print(max_profit)
weights = list(map(int,input().split()))
profits = list(map(int,input().split()))
bag_weight = int(input())
n = len(weights)
grknap(weights,profits,bag_weight,n)