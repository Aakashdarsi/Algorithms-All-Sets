def max_activities(start_times,end_times):
    i = 0 # pointer for iterating over the end times
    print(i,end=" ")#first activity is always selected
    for j in range(len(start_times)):
        if start_times[j] >= end_times[i]:
            print(j,end=" ")
            i = j 




start_times = list(map(int,input().split()))
end_times = list(map(int,input().split()))
max_activities(start_times,end_times)