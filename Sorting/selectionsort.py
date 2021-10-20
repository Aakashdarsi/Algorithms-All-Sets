def selection_sort(array):
    for i in range(len(array)-1):
        index = i

        for j in range(i+1, len(array)):
            if array[index]>array[j]:
                index = j
        if array[i]>array[index]:
            array[i],array[index] = array[index], array[i]
    print(array)

array = list(map(int,input().split()))
selection_sort(array)