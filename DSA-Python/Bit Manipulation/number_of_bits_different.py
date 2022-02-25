#https://practice.geeksforgeeks.org/problems/bit-difference-1587115620/1#
#https://www.youtube.com/watch?v=uIX_dsXwV8U

class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ##Your code here
        n = a^b 
        count = 0 
        while n!=0:
            if n&1 == 1:
                count = count +1
            n = n>>1
        return count
