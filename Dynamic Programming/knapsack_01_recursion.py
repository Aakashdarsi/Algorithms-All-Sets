def knapsack(weights, profits, bag_weight, N):
    if N ==0 or bag_weight == 0:
        return 0 
    elif weights[N-1] >bag_weight:
        return knapsack(weights,profits,bag_weight,N-1)
    else:
        return max(knapsack(weights, profits, bag_weight, N-1),profits[N-1]+knapsack(weights, profits, bag_weight - weights[N-1],N-1))




weights = [3,2,4]
profits = [6,8,7]
bag_weight = 8
result = knapsack(weights,profits,bag_weight,len(weights))
print(result)