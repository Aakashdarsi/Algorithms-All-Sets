weights = list(map(int,input().split()))
profits = list(map(int,input().split()))
bag_wt = int(input())
n = len(weights)
dp_table  = [[-1 for i in range(bag_wt+1)]for j in range(n+1)]
for i in range(n+1):
    dp_table[i][0] = 0 
for i in range(bag_wt+1):
    dp_table[0][i] = 0
for i in range(1,n+1):
    for j in range(1,bag_wt+1):
        if weights[i-1] > j :
            dp_table[i][j] = dp_table[i-1][j]
        else:
            dp_table[i][j] = max(dp_table[i-1][j],profits[i-1]+dp_table[i-1][j-weights[i-1]])
print(dp_table[n][bag_wt])
print("Dp table is as follows ... ")
for i in range(n+1):
    for j in range(bag_wt+1):
        print(dp_table[i][j],end = "|")
    print("\n")
#Time Complexity is O(N*bag_wt)