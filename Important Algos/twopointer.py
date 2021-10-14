def result(array, sum_req):
    if len(array) == 1:
        if array[0] == sum_req:
            return True
        return False
    else:
        low = 0
        high = len(array)-1
        while low < high:
            if array[low]+array[high] == sum_req:
                return [array[low],array[high]]
            elif array[low] + array[high] > sum_req:
                high -= 1
            elif array[low] + array[high] < sum_req:
                low += 1
        return "Not Found anything"


array = list(map(int, input().split()))
sum_req = int(input())
print(result(array, sum_req))