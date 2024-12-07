found_sequences = set()

for row in range(nRows):
    for col in range(nCols):
        if matrix[row][col] == "X":
            q.append((row, col, "", set()))

            while q:
                r, c, msg, visited = q.popleft()

                if len(msg) < 1:
                    search = "X"
                else:
                    search = letterMap.get(msg[-1])

                if matrix[r][c] != search:
                    continue

                newMsg = msg + matrix[r][c]
                visited.add((r, c))

                if newMsg == "XMAS":
                    # Record the sequence uniquely by starting point and direction
                    sequence_key = (row, col, tuple(visited))
                    if sequence_key not in found_sequences:
                        found_sequences.add(sequence_key)
                        xmasCount += 1
                        print(f"Unique 'XMAS' found at ({row}, {col})")
                    continue

                for dx, dy in directions:
                    newRow, newCol = r + dx, c + dy
                    if isValid(newRow, newCol, nRows, nCols, visited):
                        q.append((newRow, newCol, newMsg, visited.copy()))

print(f"Total unique XMAS sequences found: {xmasCount}")
