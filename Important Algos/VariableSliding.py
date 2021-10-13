def result(array, req_sum):
    curr_sum = 0
    window_start = 0
    window_end = 0
    size_of_array = len(array)
    while window_end<size_of_array:
        while (curr_sum>req_sum) and (window_start < window_end-1) :
            curr_sum -=array[window_start]
            window_start+=1
        if curr_sum == req_sum :
            return (window_start, window_end-1)
        if window_end<size_of_array:
            curr_sum+=array[window_end]
        window_end += 1






array = list(map(int, input().split()))
req_sum = int(input())
print(result(array, req_sum))