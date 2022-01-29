def diognal_traversal(matrix,rows,colums):
    for k in range(0,rows):
        i = k 
        j = 0 
        while i>= 0:
            print(matrix[i][j],end=" ")

            i = i-1 
            j +=1 
        print()
    for k in range(1,colums):
        i = rows-1 
        j = k 
        while j <colums:
            print(matrix[i][j],end=" ")
            i = i-1 
            j += 1 
        print()
    