# Approach 1
def target_sum(array,target):
    l = []
    for i in array:
        if target-i in array:
            return (i,target-i)
        else:
            l.append(i)
a = list(map(int,input().split()))
target = int(input())
print(target_sum(a,target))

# Approach 2
def target_sum(array,target):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if i+j == target:
                return i,j
    return 'Not found !!!!! '