def spiral(rows,cols,matrix):
    last_row = rows - 1 
    last_cols = cols - 1 
    k = 0
    l = 0 
    while k <= last_row and l <= last_cols:
        for i in range(0,last_cols+1):
            print(matrix[k][i])
        k += 1 
        for i in range(k,last_row+1):
            print(matrix[i][last_cols],end=" ")
        last_cols -=1 
        if k <= last_row:
            for i in range(last_cols,l-1,-1):
                print(matrix[last_row][i])
            last_row -= 1 
        if l <= last_cols:
            for i in range(last_row,k-1,-1):
                print(matrix[i][l])
            l += 1 
    

