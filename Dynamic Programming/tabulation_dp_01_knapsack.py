weights = [1,2,3]
profits = [4,5,6]
bag_weight = 5 
table = [[-1 for i in range(bag_weight+1)] for j in range(len(weights)+1)]
for i in range(0,len(weights)+1):
    for j in range(0,bag_weight+1):
        if i==0 or j==0:
            table[i][j] = 0
        elif weights[i-1] > j:
            table[i][j] = table[i-1][j]
        
        else:
            table[i][j] = max(table[i-1][j],profits[i-1]+table[i-1][j-weights[i-1]])
print(table[len(weights)][bag_weight])