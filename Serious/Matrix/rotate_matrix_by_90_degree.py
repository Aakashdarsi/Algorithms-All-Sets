#https://www.youtube.com/watch?v=Y72QeX0Efxw
def rotate_matrix(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if i != j :
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j] # Transpose Of matrix created
    
    for i in matrix:
        i.reverse()
    print(matrix)