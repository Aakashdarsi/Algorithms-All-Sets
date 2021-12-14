def knapsack(weights,profits,bag_weight,n):
    result = 0 
    if bag_weight == 0 or n ==0 :
        return 0 
    if table[n][bag_weight] != -1:
        return table[n][bag_weight]
    elif weights[n-1] > bag_weight:
        return knapsack(weights,profits,bag_weight,n-1)
    else:
        result =  max(knapsack(weights,profits,bag_weight,n-1),profits[n-1]+knapsack(weights,profits,bag_weight-weights[n-1],n-1))
        table[n][bag_weight] = result
    return result





weights = list(map(int, input().split()))
profits = list(map(int, input().split()))
bag_weight = int(input())
n = len(weights)
table = [[-1 for i in range(bag_weight+1)] for j in range(n+1)]
result = knapsack(weights,profits,bag_weight,n)
print(result)