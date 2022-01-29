#https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/
def common_elements_in_matrix(matrix):
    first_row = matrix[0] # Take first row values as keys for the hash map
    map = {} # initialise the map
    for i in first_row: 
        if i not in map: # IF THAT VALUE NOT PRESENT IN MAP THEN INITIALISE THE KEY AND ITS VALUE AS 1
             map[i] = 1 
    for i in range(1,len(matrix)): #START TRAVERSING FROM FIRST ROW
        for j in range(len(matrix[0])):
            if matrix[i][j] in map:
                if i == map[i]:# IF ROW VALUE IS EQUAL TO THAT PARTICULAR KEY'S VALUE THEN INCREMENT
                    map[i]+=1 

    for i in sorted(map):
        if map[i] == len(matrix): #PRINT THE KEYS HAVING VALUE AS NUMBER OF ROWS
            print(i,end=" ")       
