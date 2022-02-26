def knapsack_unbounded(weights,profits,bag_weight,n):
    if n == 0 or bag_weight == 0:
        return 0
    if weights[n-1] > bag_weight:
        return knapsack_unbounded(weights,profits,bag_weight,n-1)
    else:
        return max(knapsack_unbounded(weights,profits,bag_weight,n-1),profits[n-1]+knapsack_unbounded(weights,profits,bag_weight-weights[n-1],n))


weights = list(map(int,input().split()))
profits = list(map(int,input().split()))
bag_weight = int(input())
n = len(weights)
print(knapsack_unbounded(weights,profits,bag_weight,n))