# Naive approach 1
# -1 5 10 28 3 :- I/p
# 26 134 135 15 17 :- I/P
# [28, 26] :- O/P
# def smallest_diiference(array_1,array2):
#     min_val = float("+inf")
#     min_pair = None
#     for i in range(len(array_1)):
#         for j in range(len(array2)):
#             differenece = abs(array_1[i]-array2[j])
#             if differenece < min_val :
#                 min_val = differenece
#                 min_pair = [array_1[i],array2[j]]
#     print(min_pair)
#     print(min_val)

# l1 = list(map(int,input().split()))
# l2 = list(map(int,input().split()))
# smallest_diiference(l1,l2)
# This program works but it has time complexity of O(N^2)

# ----------------------------------------------------------------------------

# If two numbers are equal to each other than they are 
# Sort the array
# Set i as pointer at array 1
# set j as pointer in array 2
# if i <=j increment i position by1 
# otherwise increment j by position 1 
def smallest_diff(array1,array2):
    array1.sort()
    array2.sort()
    index_1 = 0 
    index_2 = 0 
    smal_dif = float("inf")
    cur_dif = float('inf')
    smal_pair = []
    while index_1 < len(array1) and index_2 < len(array2):
        first_num = array1[index_1]
        second_num = array2[index_2]
        if first_num < second_num:
            cur_dif = second_num - first_num
            index_1 += 1 
        elif second_num < first_num:
            cur_dif = first_num - second_num
            index_2 += 1 
        else:
            return [first_num,second_num]
        if smal_dif > cur_dif:
            smal_dif = cur_dif
            smal_pair = [first_num,second_num]
    return smal_pair

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(smallest_diff(l1,l2))

# Tine complexity is O(NlogN) + O(MlogM) as for sorting two array's. Merge sort !!!!!!!