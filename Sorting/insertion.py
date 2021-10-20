def insertion(a): # we will check previous values 
    for i in range(1,len(a)):
        present_value = a[i]
        previous_value = i - 1 
        while previous_value >=0 and a[previous_value]>present_value:
            a[previous_value+1] = a[previous_value]
            previous_value-=1
        a[previous_value+1] = present_value 
    print(a)


a = list(map(int,input().split()))
insertion(a)