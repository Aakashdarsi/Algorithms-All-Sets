def merge_sort(array):
    if len(array)<=1:
        return  array
    left = merge_sort(array[0:len(array)//2])
    right = merge_sort(array[len(array)//2:])
    print()



array = list(map(int, input().split()))
merge_sort(array)