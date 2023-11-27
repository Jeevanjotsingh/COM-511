'''# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

k = 2  # Reverse every 2nd row

#Loop for reversing matrix
for i in range(0, len(matrix), k):
    matrix[i:i+k] = reversed(matrix[i:i+k])
    
# Print the result
print("Reversed Matrix")
for row in matrix:
    print(row)'''

# Taking input for the matrix size and elements
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter matrix elements row by row:")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Taking input for the column number to reverse
k = int(input("Enter kth column to reverse (1-based index): "))
k = k - 1  # Adjusting to 0-based index

# Reversing k-th column in the matrix
column_values = [row[k] for row in matrix]
reversed_column = list(reversed(column_values))
for i in range(len(matrix)):
    matrix[i][k] = reversed_column[i]

# Printing the modified matrix
print("Modified Matrix : ")
for row in matrix:
    print(row)
