weights = list(map(int,input().split()))
profits = list(map(int,input().split()))
n = len(weights)
bag_wt = int(input())
dp_table = [[-1 for i in range(bag_wt+1)]for j in range(n+1)]
for i in range(bag_wt+1): # If number of elemnts is zero and bag_wt != 0 then return 0
    dp_table[0][i] = 0 

#If no_of_ele is non zero and bag_weight is zero profit woul be zero
for i in range(n+1):
    dp_table[i][0] = 0 

for i in range(1,n+1):
    for j in range(1,bag_wt+1):
        if weights[i-1]>j:
            dp_table[i][j] = dp_table[i-1][j]
        else:
            dp_table[i][j] = max(dp_table[i-1][j],profits[i-1]+dp_table[i][j-weights[i-1]])
print(dp_table[n][bag_wt])

