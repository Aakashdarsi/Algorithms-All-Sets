set_ele = list(map(int,input().split()))
sum_to = int(input())
n = len(set_ele)
dp = [[False for i in range(sum_to+1)]for j in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1 # Number of elements to be zero or non zero but sum to be found is zero 
for i in range(1,sum_to+1): # sum is non zero number of elements  are zero then False
    dp[0][i] = 0


for i in range(1,n+1):
    for j in range(1,sum_to+1):
        if set_ele[i-1]>j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-set_ele[i-1]]
print(dp[n][sum_to])
print("DP TABLE")
for i in range(n+1):
    for j in range(sum_to+1):
        print(dp[i][j],end="| ")
    print()