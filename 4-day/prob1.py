from collections import deque
matrix = []
xmasCount = 0
with open("input.txt") as fileIn:
    for line in fileIn:
        row = list(line.strip())
        print(row)
        matrix.append(row)
        
letterMap = {'' : 'X', 'X' : 'M', 'M':'A', 'A':'S'}
directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
visited = set()
nRows = len(matrix)
nCols = len(matrix[0])
def isValid(col, row, nRows, nCols, r,c ):
    return 0 <= row < nRows and 0 <= col < nCols

q = deque()


for row in range(nRows):
    for col in range(nCols):
        if matrix[row][col] == "X":
            q.append((row, col, "", [],[]))
            #visited.add((row,col))
            
            while q:
                r, c, msg, path, direction = q.popleft()
                
                #print(row, col)
                if len(msg) < 1:
                    search = "X"
                else:
                    search = letterMap.get(msg[-1])
                #print(matrix[r][c], search)
                newPath = path + [str((r,c))]
                if matrix[r][c] != search:
                    continue
                newMsg = msg.strip("") + matrix[r][c]
                
                if newMsg == "XMAS":
                    print(newMsg)
                    if ''.join(newPath) in visited:
                        continue
                    xmasCount += 1
                    visited.add(''.join(newPath))
                    print(xmasCount, ''.join(newPath))
                    continue
                if (len(direction) < 1):
                    
                    for dx, dy in directions:
                        newRow, newCol = r + dx, c + dy
                        if isValid(newRow, newCol, nRows, nCols, r, c):
                            q.append((newRow, newCol, newMsg, newPath,[(dx,dy)]))
                else: 
                    newRow,newCol = r + direction[0][0], c + direction[0][1]
                    if isValid(newRow, newCol, nRows, nCols, r, c):
                            q.append((newRow, newCol, newMsg, newPath, direction))
                        
print(xmasCount)
                    
                