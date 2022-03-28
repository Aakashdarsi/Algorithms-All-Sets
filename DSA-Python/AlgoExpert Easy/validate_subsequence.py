# Approach 1 (Using for loop)

# All of the elements in subsequence array and ashould also be in same sequence 




def validate_subsequence(array,subseq):
    start = 0  # until we dont find match we don't move in subsequence  
    for i in array:
        if subseq[start] == i : # Time complexity is O(N) Space complexity O(1)
            start += 1
    return len(subseq) == start 
array = list(map(int,input().split()))
subseq = list(map(int,input().split()))
print(validate_subsequence(array,subseq))


# Using while loop
def validate_subsequence(array,subseq):
    arrIndex =0 
    seqIndex = 0
    while arrIndex <len(array) and seqIndex < len(subseq):
        if array[arrIndex] == subseq[seqIndex]:
            seqIndex += 1 
        arrIndex += 1 
    return seqIndex == len(subseq)