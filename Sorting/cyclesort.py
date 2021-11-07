# When the range is given from (1 to N) use cyclic sort ---->>>> VVVVVV IMP
def cyclic(array):
    if len(array) == 0:
        print("No ele")
    elif len(array) == 1:
        print(array)
    else:
        start_value =0
        while start_value < len(array):
            correct = array[start_value] - 1
            if array[start_value] != array[correct]:
                array[start_value],array[correct] = array[correct],array[start_value]
            else:
                start_value+=1
        print(array)



array = list(map(int,input().split()))
cyclic(array)
