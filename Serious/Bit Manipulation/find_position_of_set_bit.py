#https://practice.geeksforgeeks.org/problems/find-position-of-set-bit3706/1#
# If the number is power of 2 Then only  we can see that there exists only 1 bit in a number otherwise you do have more Bits in  it
#For checking the whether its a power of 2 or not use n&(n-1) if its result = 0 power of 2 othewise not a power of 2

class Solution:
    def findPosition(self, N):
        # code here 
        if N ==0:
            return -1
        if N&(N-1) == 0:
            count = 0
            while N!= 0:
                count +=1
                N = N>>1
            return count
        return -1