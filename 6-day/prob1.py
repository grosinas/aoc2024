import sys

class Problem:
    def __init__(self, filename):
        self.filename = filename
        self.directions = [(-1,0), (0,1), (1,0), (0,-1)]
        self.graph = []
        try:
            with open(self.filename) as file:
                for line in file:
                    self.graph.append([c for c in [str(s) for s in line.split()][0]])
            print(self.graph[0])
        
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
            
        self.startingPoint = (0,0)
        for i in range(len(self.graph)):
            for j in range(len(self.graph[0])):
                if '^' in self.graph[i][j]:
                    self.startingPoint = (i,j)
                    print(self.startingPoint)
            
        self.nRows = len(self.graph)
        self.nCols = len(self.graph[0])
        self.visited = set()
    
    def outOfBounds(self, row, col):
        return row < 0 or row >= self.nRows or col < 0 or col >= self.nCols
    
    """ Solution to AOC 2024 Day 6, Problem 1
    """
    def problem1(self):
        currDir = 0
        row, col = self.startingPoint
        print(row, col)
        while True:
            dx, dy = self.directions[currDir]
            if (row,col) not in self.visited:
                self.visited.add((row,col))
            nextRow, nextCol = row + dx, col + dy
            #print(nextRow,nextCol)
            if (self.outOfBounds(nextRow,nextCol)):
                print(len(self.visited))
                break
            elif self.graph[nextRow][nextCol] == "#":
                nextRow, nextCol = row, col
                currDir = (currDir + 1) % (len(self.directions))
            else: 
                row, col = nextRow, nextCol
                
    def findLoop(self, grid):
        rowColDirSet = set()
        currDir = 0
        row, col = self.startingPoint
        while True:
            dx, dy = self.directions[currDir]
            
            # If in a run of the traversal we have
            # reached the same spot, when moving in the same
            # Direction as when we reached it before
            # It means that we are in a loop, so 
            # TRUE is returned
            if (row,col,currDir) in rowColDirSet:
                return True
            else:
                rowColDirSet.add((row,col,currDir))
            nextRow, nextCol = row + dx, col + dy
            
            # IF we are not in a loop, it means that
            # at some point the guard will be out of bounds
            # So By returning FALSE after this guard
            # Ensures that this loop always terminates
            if (self.outOfBounds(nextRow,nextCol)):
                return False
                break
            elif grid[nextRow][nextCol] == "#":
                nextRow, nextCol = row, col
                currDir = (currDir + 1) % (len(self.directions))
            else: 
                row, col = nextRow, nextCol
                    
    def problem2(self):
        counter = 0
        # For all the nodes visited in the 
        # Original Traversal of the Graph
        # Find if placing a block there
        # TRUE is returned
        for (row, col) in self.visited:
            grid = self.graph
            grid[row][col] = "#"
            #print(grid)
            if (self.findLoop(grid)):
                counter += 1
                
            grid[row][col] = "."
        print(counter)
            
                    

if __name__ == "__main__":#
    if len(sys.argv) != 2:
        print("Usage: python prob1.py <filename>")
    else:
        filename = sys.argv[1]
        problem = Problem(filename)
        problem.problem1()
        problem.problem2()