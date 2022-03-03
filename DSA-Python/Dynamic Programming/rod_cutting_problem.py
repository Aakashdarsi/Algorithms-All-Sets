#Rod Cutting problem
# Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if the length of the rod is 8 and the values of different pieces are given as the following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

# length   | 1   2   3   4   5   6   7   8  
# --------------------------------------------
# price    | 1   5   8   9  10  17  17  20
# And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1) 
# https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture12.pdf
def rod_cut(profits,n):
    dp = [[0 for i in range(len(profits)+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(n+1):
        dp[0][i] = 0
    for i in range(1,n+1):
        for j in range(1,len(profits)+1):
            if i > j :
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],profits[i-1]+dp[i][j-i])
    print(dp[n][n])


profits = list(map(int,input().split(',')))
n = int(input())
rod_cut(profits,n)