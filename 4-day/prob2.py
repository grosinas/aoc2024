from collections import deque
matrix = []
xmasCount = 0
with open("input.txt") as fileIn:
    for line in fileIn:
        row = list(line.strip())
        print(row)
        matrix.append(row)
        
valid = set()
valid.add("M")
valid.add("S")
        
def diagonalCheck(row, col):
    return 0 <= row - 1 and row + 1 < nRows and 0 <= col - 1 and col + 1 < nCols
        
count = 0
nRows = len(matrix)
nCols = len(matrix[0])
for row in range(nRows):
    for col in range(nCols):
        if matrix[row][col] == "A":
            if not diagonalCheck(row, col):
                continue
        
            if matrix[row+1][col-1] in valid and  matrix[row-1][col+1] in valid and matrix[row-1][col+1] != matrix[row+1][col-1]:
               if matrix[row-1][col-1] in valid and  matrix[row+1][col+1] in valid and matrix[row-1][col-1] != matrix[row+1][col+1]:
                   count += 1
print(count)