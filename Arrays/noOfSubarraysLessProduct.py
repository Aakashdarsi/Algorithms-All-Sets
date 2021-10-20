def result(array,req_pr):
    if len(array)==0:
        return "Cannot be find here"
    elif len(array) == 1:
        if array[0]<req_pr:
            return 1
    else:
        start_pointer = 0 
        end_pointer = 0 
        product = 1 
        counter = 0
        while end_pointer < len(array):
            product*=array[end_pointer]
            if product > req_pr:
                product = product//array[end_pointer]
                start_pointer = start_pointer+1 
                end_pointer = start_pointer
            elif product < req_pr:
                counter +=1 
                end_pointer = end_pointer+1
        return counter





array = list(map(int,input().split()))
req_pr = int(input())
print(result(array,req_pr))