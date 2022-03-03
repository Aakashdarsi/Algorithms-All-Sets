#Leetcode 518
# Max Number of Ways
# If in quesetion if they ask max number of ways or choies then use + operator
coins = list(map(int,input().split()))
sum_to = int(input())
n = len(coins)
dp = [[-1 for i in range(sum_to+1)]for j in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1 

for i in range(sum_to+1):
    dp[0][i] = 0 

for i in range(1,n+1):
    for j in range(1,sum_to+1):
        if coins[i-1]>j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]+dp[i][j-coins[i-1]]
print(dp[n][sum_to])