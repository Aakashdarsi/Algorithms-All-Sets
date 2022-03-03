from audioop import reverse

# Greedy approach fails in some conditions
def min_coins(coins,value):
    coins.sort(reverse = True)
    n = len(coins)
    count = 0 
    t= value
    for i in range(n):
        while t >= coins[i]:
            t-= coins[i]
            count += 1
    print(count)


coins = list(map(int,input().split()))
value = int(input())
min_coins(coins,value)