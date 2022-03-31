# Very Very helpful for other type of problems in array 

# [12,3,1,2,-6,5,-8,6] target 0 

# Approach 1 
# def three_sum_pairs(array,target):
#     for i in range(1,len(array)-2):
#         for j in range(i+1,len(array)-1):
#             for k in range(j+1,len(array)):
#                 if array[i]+array[j]+array[k] == target:
#                     print([array[i],array[j],array[k]])
# l = list(map(int,input().split()))
# target = int(input())
# three_sum_pairs(l,target)

# Here the time complexity would be O(N^3) so we neeed to optimise the solution . The optimised  solution is helpful for the other array type problems

# ----------------------------------------------------------------------

# Approach 2
# Steps :- 
# 1. sort the array in ascending order 
# 2. using left and right pointer and try to find the answer
# what is pointing of sort 
def three_sum_optimal(array,target): # time complexity is O(N^2) using two pointer 
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        left = i+1 
        right = len(array) - 1 
        while left < right :
            current_sum = array[i]+array[left]+array[right]
            if current_sum == target:
                triplets.append([array[i],array[left],array[right]])
                left +=1 
                right -= 1
            elif current_sum > target:
                right -= 1
            elif current_sum < target :
                left += 1 
    print(triplets)

l = list(map(int,input().split()))
target = int(input())
three_sum_optimal(l,target)