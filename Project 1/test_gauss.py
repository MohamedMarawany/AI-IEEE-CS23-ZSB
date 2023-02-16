def gauss_jordan_elimination(matrix): 
    n = len(matrix) 
  
    for i in range(0, n): 
        for j in range(0, n): 
            if (i != j): 
                ratio = matrix[j][i] / matrix[i][i] 
  
                for k in range(0, n + 1): 
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k] 

    for i in range(n): 
        a = matrix[i][i] 

        for j in range (0, n + 1): 
            matrix[i][j] = matrix[i][j] / a

    return matrix

print(gauss_jordan_elimination([[0, 2, 1, 4], [1, 1, 2, 6], [2, 1, 1, 7]]))