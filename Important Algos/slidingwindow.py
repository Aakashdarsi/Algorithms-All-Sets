def sliding(array, k):
    curr_sum = 0   # Approach of sliding window method
    max_sum = 0
    for i in range(k):
        curr_sum += array[i]
    max_sum = curr_sum
    for i in range(k, len(array)):
        curr_sum = (curr_sum - array[i - k]) + array[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum


array = list(map(int, input().split()))
k = int(input())
result = sliding(array, k)
print(result)
# Time complexity of this algorithm is O(n)
