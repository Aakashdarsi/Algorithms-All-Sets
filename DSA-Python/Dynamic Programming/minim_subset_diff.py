
#Minimum subset sum difference 

def min_difference(set,sum_to,n):
    dp = [[False for i in range(sum_to+1)]for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True 
    for i in range(1,sum_to+1):
        dp[0][i] = False 
    
    for i in range(1,n+1):
        for j in range(1,sum_to+1):
            if set[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-set[i-1]]
    min_difference_val = float("+inf") 
    for i in range(0,(sum_to//2)+1):
        first = i 
        second = sum_to - i
        
        if dp[n][i] == True and min_difference_val>abs(first-second):
            min_difference_val = abs(first-second)
    print(min_difference_val)
    



set = list(map(int,input().split()))
sum_to = sum(set)
n = len(set)
min_difference(set,sum_to,n)