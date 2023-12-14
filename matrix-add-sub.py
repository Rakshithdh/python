def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    
    result = []
    for i in range(rows):
        # Initialize an empty row for the result matrix
        result_row = []
        for j in range(cols):

            # Add the corresponding elements from matrix1 and matrix2
            result_row.append(matrix1[i][j] + matrix2[i][j])
        # Add the row to the result matrix
        result.append(result_row)

    return result

def subtract_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    result = []
    for i in range(rows):
        # Initialize an empty row for the result matrix
        result_row = []
        for j in range(cols):
            # Subtract the corresponding elements from matrix1 and matrix2
            result_row.append(matrix1[i][j] - matrix2[i][j])
        # Add the row to the result matrix
        result.append(result_row)
    
    return result

# Rest of the code remains unchanged
# ...


# Get input for the matrices
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix1 = []
print("Enter elements for matrix1:")
for i in range(rows):
    row = [int(input()) for _ in range(cols)]
    matrix1.append(row)

matrix2 = []
print("Enter elements for matrix2:")
for i in range(rows):
    row = [int(input()) for _ in range(cols)]
    matrix2.append(row)

# Perform addition and subtraction
sum_result = add_matrices(matrix1, matrix2)
difference_result = subtract_matrices(matrix1, matrix2)

# Display the results
print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nSum of Matrices:")
for row in sum_result:
    print(row)

print("\nDifference of Matrices:")
for row in difference_result:
    print(row)
