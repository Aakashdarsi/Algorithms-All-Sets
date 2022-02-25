# https://practice.geeksforgeeks.org/problems/power-of-2-1587115620/1#
# Bit Fiddling Technique n&(n-1) if result is zero then its a power of 2 otherwise its not a power of 2 .Very Important technique in Bit manipulation
#https://www.youtube.com/watch?v=YZRlBjyUnKU
class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        if n == 0:
            return False
        else:
            if( n &(n-1)) != 0:
                return False
            else:
                return True
