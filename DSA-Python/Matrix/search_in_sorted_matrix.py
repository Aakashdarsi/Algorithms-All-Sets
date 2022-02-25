class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        
        n = len(matrix[0])
        i  = 0
        j = n -1
        while i<m and j>=0:
            if matrix[i][j] == target:
                return True
            elif target< matrix[i][j]:
                j -= 1
            elif target>matrix[i][j]:
                i +=1
        return False
