# 416. Partition Equal Subset Sum
# Medium

# 6384

# 106

# Add to List

# Share
# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

def isSubset(a,n,half):
    if half == 0:
        return True 
    if n == 0:
        return False
    elif a[n-1] > half:
        return isSubset(a,n-1,half)
    else:
        return isSubset(a,n-1,half) or isSubset(a,n-1,half-a[n-1])


def partition(a,n):
    sume = sum(a)
    if sume&1 ==1:
        return False
    else:
        return isSubset(a,n,sume//2)


a = [1,2,3]
n = len(a)
res = partition(a,n)
print(res)