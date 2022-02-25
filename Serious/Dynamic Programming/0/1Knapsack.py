#https://www.youtube.com/watch?v=kvyShbFVaY8&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=3
#https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
def knapsack(weight,profit,n,bag_wt):
    if n == 0 or bag_wt == 0:
        return 0 
    if weight[n-1] > bag_wt:
        return knapsack(weight,profit,n-1,bag_wt) # if the item weight is greater than the bag weight then it can't be included
    else:
        return max(
            profit[n-1]+knapsack(weight,profit,n-1,bag_wt-weight[n-1]),
            knapsack(weight,profit,n-1,bag_wt))

    
    


weight = list(map(int,input().split()))
profit = list(map(int,input().split()))
n = len(weight)
bag_wt = int(input())
print(knapsack(weight,profit,n,bag_wt))