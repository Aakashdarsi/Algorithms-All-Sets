def knapsackc_memoiseed(weights,profits,bag_weight,n):
    result = 0
    if weights ==0 or n ==0:
        return 0 
    
    if weights[n]>bag_weight:
        return 0 
    if look_up_table[n][bag_weight] != -1:
        return look_up_table[n][bag_weight]
    else:
        result = max(knapsackc_memoiseed(weights,profits,bag_weight,n-1),profits[n]+knapsackc_memoiseed(weights,profits,bag_weight-weights[n],n-1))
        look_up_table[n][bag_weight] = result
    return look_up_table[n][bag_weight]




weights = [3,2,4]
profits = [6,8,7]
bag_weight = 8
look_up_table = [[-1 for i in range(bag_weight+1)]for j in range(len(weights)+1)]
result = knapsackc_memoiseed(weights,profits,bag_weight,len(weights)-1)
print(result)
