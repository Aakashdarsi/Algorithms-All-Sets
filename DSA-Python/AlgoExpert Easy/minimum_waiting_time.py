# https://www.youtube.com/watch?v=Sf3eiO12eJs

def min_waiting(queries):
    queries.sort()
    total_waiting_time = 0 
    for index,duration in enumerate(queries):
        queries_left =  len(queries) - (index+1)
        total_waiting_time += duration*queries_left
    return total_waiting_time

l = list(map(int,input().split()))
print(min_waiting(l))