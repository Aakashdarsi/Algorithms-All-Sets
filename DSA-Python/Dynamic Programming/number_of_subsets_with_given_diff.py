#Count the number of subsets with given difference


def no_of_subset_with_given_diff(set,to_find_sum):
    n = len(set)
    dp = [[0 for i in range(to_find_sum+1)]for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1 
    for i in range(1,to_find_sum+1):
        dp[0][i] = 0 
    for i in range(1,n+1):
        for j in range(1,to_find_sum+1):
            if set[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]+dp[i-1][j-set[i-1]]
    print(dp[n][to_find_sum])


set = list(map(int,input().split()))
difference = int(input())
sum_ele = sum(set)
to_find_sum  = (difference+sum_ele)//2
no_of_subset_with_given_diff(set,to_find_sum)