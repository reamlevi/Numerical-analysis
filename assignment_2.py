"""
Authors : ream levi - 205866692 , yarden shaked - 206789885.
GitHub : 
Assignment 2 - Numeric Analytics
"""

def square_matrix(matrix)->bool:
    """
    Check if the given matrix is a square matrix.

    Parameters:
    matrix (list of lists): The matrix to be checked.

    Returns:
    bool: True if the matrix is square, False otherwise.
    """
    num_rows = len(matrix)
    for row in matrix:
        if len(row)!= num_rows:
            print("Matrix must be square")
            return False
    return True        

def determinant(matrix) -> int:
    """
    Calculate the determinant of a square matrix.

    Parameters:
    matrix (list of lists): The square matrix.

    Returns:
    int: The determinant of the matrix.
    """
    num_rows = len(matrix)
    if num_rows == 2:  # base case for 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(num_rows):
            det += ((-1) ** i) * matrix[0][i] * determinant(smaller_matrix(matrix, 0, i))
        return det

def smaller_matrix(matrix, row, col)-> list[list[int]]:
    """
    This function creates a smaller matrix by removing a specific row and column from the given matrix.

    Parameters:
    matrix (list of lists): The original matrix.
    row (int): The index of the row to be removed.
    col (int): The index of the column to be removed.

    Returns:
    list of lists: The smaller matrix after removing the specified row and column.
    """
    smaller = []
    smaller_raw = 0
    for i in range(len(matrix)):
        if i != row:
            smaller.append(matrix[i][:])  # add all rows except the specified row
            smaller[smaller_raw].pop(col)  # remove the specified column
            smaller_raw += 1
    return smaller        

def inverse(matrix)-> list[list[float]]:
    """
    Calculate the inverse of a square matrix.
 
    Parameters:
    matrix (list of lists): The square matrix.
    
    Returns:
    list of lists: The inverse of the matrix.
    """
    num_rows = len(matrix)
    identity_matrix = identity_calc(num_rows)

    for i in range(num_rows):
        # Divide the row by the pivot element
        pivot = matrix[i][i]
        for j in range(num_rows):
            matrix[i][j] /= pivot
            identity_matrix[i][j] /= pivot

        # Subtract the pivot row from other rows
        for k in range(num_rows):
            if k != i:
                factor = matrix[k][i]
                for j in range(num_rows):
                    matrix[k][j] -= factor * matrix[i][j]
                    identity_matrix[k][j] -= factor * identity_matrix[i][j]

    return identity_matrix

def identity_calc(num_rows_and_cols):
    """
    This function generates an identity matrix of size num_rows_and_cols x num_rows_and_cols.

    Parameters:
    num_rows_and_cols (int): The number of rows and columns in the identity matrix.

    Returns:
    list of lists: A num_rows_and_cols x num_rows_and_cols identity matrix.
    """
    return [[float(i == j) for j in range(num_rows_and_cols)] for i in range(num_rows_and_cols)]
 




        

A = [[1,-1,-2],[2,-3,-5],[-1,3,5]]

print(square_matrix(A))
print(determinant(A))

print(inverse(A))


