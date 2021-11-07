# bubble sort worst case -> O(N^2) Best case -> O(N)


def bubble(array):
    if len(array) == 0:
        print("No elements in array")
    elif len(array) == 1:
        print(array)
    else:
        for i in range(len(array)-1):
            swapped = False
            for j in  range(1,len(array)-i):
                if array[j]<array[j-1]:
                    array[j],array[j-1] = array[j-1], array[j]
                    swapped = True
            if swapped == False:
                break
        print(array)





array = list(map(int,input().split()))
bubble(array)