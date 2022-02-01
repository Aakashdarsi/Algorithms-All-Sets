#https://practice.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1#
#https://www.youtube.com/watch?v=8ZJ8xhJNtU0
def twoOddNum(self, Arr, N):
        # code here
        x = Arr[0]
        first = 0 
        second = 0
        for i in range(1,N):
            x ^=Arr[i]
        set_bit = x & ~(x-1)
        for i in range(N):
            if Arr[i]&set_bit:
                first ^=Arr[i]
            else:
                second ^=Arr[i]
        if first > second:
            return first,second
        else:
            return second,first