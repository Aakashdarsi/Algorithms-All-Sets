#https://www.youtube.com/watch?v=oN9g7lEsJqc&t=190s
class Solution:

    def rowWithMax1s(self,arr, n, m):
        # code here
        rows = n 
        cols = m 
        i = 0 
        j = cols-1
        max_1_r = -1
        while i<rows and j>=0:
            if arr[i][j] == 1:
                max_1_r = i 
                j -=1
            elif arr[i][j] == 0:
                i +=1
        
        return max_1_r
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends