# Its better than bubble sort because in some iterations we are skipping the things .....
# Insertion sort Best Case -> O(N) Worst case -> O(N^2)

def insertion(array):
    if len(array) == 0:
        print("No elements to sorted")
    elif len(array) == 1:
        print(array)
    else:
        for i in range(len(array) - 1):
            for j in range(i + 1, 0, -1):
                if array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
                else:
                    break
        print(array)


array = list(map(int, input().split()))
insertion(array)

