# Given an array and a positive integer k, find the first negative integer for each and every window(contiguous subarray) of size k.

# Example:

# Input:
# 2
# 5
# -8 2 3 -6 10
# 2
# 8
# 12 -1 -7 8 -15 30 16 28
# 3

# Output:
# -8 0 -6 -6
# -1 -1 -7 -15 -15 0
def result(array,window_size):
    start = 0 
    end = 0 
    cur_win_size = (end-start)+1 
    negative_list = []
    while end < len(array):
        if array[end]<0:
            negative_list.append(array[end])
        elif cur_win_size<window_size:
            end = end + 1 
        elif cur_win_size==window_size:
            if len(negative_list)==0:
                print(0)
            else:
                print(array[0])
                array.pop[0]
            start = start+1 
            end = end +1




array = list(map(int,input().split()))
window_size = int(input())
result(array,window_size)
