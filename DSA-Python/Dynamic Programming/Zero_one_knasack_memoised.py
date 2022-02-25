from curses import keyname
import re


def memoised_dp(weights,profits,bag_wt,n):
    result = 0
    if n == 0 or bag_wt == 0:
        return 0 
    if dp_table[n][bag_wt] != -1:
        return dp_table[n][bag_wt]
    if weights[n-1] > bag_wt:
        result = memoised_dp(weights,profits,bag_wt,n-1)
    else:
        result  = max(
            memoised_dp(weights,profits,bag_wt,n-1),
            profits[n-1]+memoised_dp(weights,profits,bag_wt-weights[n-1],n-1)
        )
    dp_table[n][bag_wt] = result
    return dp_table[n][bag_wt]
    








weights = list(map(int,input().split()))
profits = list(map(int,input().split()))
bag_wt = int(input())
n = len(weights)
dp_table = [[-1 for i in range(bag_wt+1)] for i in range(len(weights)+1)]
print(memoised_dp(weights,profits,bag_wt,n))