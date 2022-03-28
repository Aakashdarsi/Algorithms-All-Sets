# Time complexity is O(N^2)
# Space complexity O(1)

def insertion_sort(array):
    for i in range(1,len(array)):
        j = i 
        while j > 0 and array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
            j-=1
    return array
l = list(map(int,input().split()))
insertion_sort(l)
print(l)

