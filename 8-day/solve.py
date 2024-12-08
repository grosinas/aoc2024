import sys
from collections import defaultdict
class Problem:
    def __init__(self, filename):
        self.filename = filename
        self.mp = []
        # Parse mp input into rows of characters
        with open(filename) as fileIn:
            for line in fileIn:
                row = [c for c in str(line).strip()]
                self.mp.append(row)
        #print(self.mp)
        self.nRows = len(self.mp)
        self.nCols = len(self.mp[0])
        print("ROws: "  + str(self.nRows))
        print("COLS: " + str(self.nCols))
        
    def problem1(self):
        mp = self.mp
        sameFreq = defaultdict(set)
        sol = set()
        comparedPairs = set()
        for row in range(self.nRows):
            for col in range(self.nCols):
                val = mp[row][col]
                if val.isalnum():
                    # Add found antenna to list of found antennas 
                    sameFreq[val].add((row,col))
                    for (r, c) in sameFreq.get(val):
                        if (row, col, r, c) in comparedPairs or (r, c, row, col) in comparedPairs:
                            continue
                        if (r,c) == (row,col):
                            continue
                        diffR, diffC = r - row, c - col
                        rAnt1, cAnt1 = row + 2 * diffR, col + 2 * diffC
                        rAnt2, cAnt2 = row - diffR, col - diffC
                        
                        if self._is_valid(rAnt1, cAnt1):
                            sol.add((rAnt1,cAnt1))
                        if self._is_valid(rAnt2, cAnt2):
                            sol.add((rAnt2, cAnt2))
                        
                        comparedPairs.add((row,col,r,c))
        print(len(sol))
        
        
    def problem2(self):
        mp = self.mp
        sameFreq = defaultdict(set)
        sol = set()
        comparedPairs = set()
        for row in range(self.nRows):
            for col in range(self.nCols):
                val = mp[row][col]
                if val.isalnum():
                    # Add found antenna to list of found antennas 
                    sameFreq[val].add((row,col))
                    sol.add((row,col))
                    for (r, c) in sameFreq.get(val):
                        if (row, col, r, c) in comparedPairs or (r, c, row, col) in comparedPairs:
                            continue
                        if (r,c) == (row,col):
                            continue
                        diffR, diffC = r - row, c - col
                        rAnt1, cAnt1 = row + diffR, col + diffC
                        while self._is_valid(rAnt1, cAnt1):
                            sol.add((rAnt1, cAnt1))
                            rAnt1, cAnt1 = rAnt1 + diffR, cAnt1 + diffC        
                        
                        rAnt2, cAnt2 = row - diffR, col - diffC
                        
                        while self._is_valid(rAnt2, cAnt2):
                            sol.add((rAnt2, cAnt2))
                            rAnt2, cAnt2 = rAnt2 - diffR, cAnt2 - diffC    
                        
                        comparedPairs.add((row,col,r,c))
        print(len(sol))            
        for i in range(self.nRows):
            for j in range(self.nCols):
                if (i,j) in sol:
                    mp[i][j] = "#"
            print(mp[i])
                
    def _is_valid(self, row, col):
        return 0 <= row < self.nRows and 0 <= col < self.nCols
        
if __name__ == "__main__":#
    if len(sys.argv) != 2:
        print("Usage: python prob1.py <filename>")
    else:
        filename = sys.argv[1]
        problem = Problem(filename)
        problem.problem2()