import sys

class Problem:
    def __init__(self, filename):
        self.filename = filename
        self.equations = []
        
        with open(filename) as fileIn:
            for line in fileIn:
                line = line.strip()
                eqn = line.split(":")
                eqn[1] = [int(a) for a in eqn[1].strip(" ").split(" ")]
                eqn[0] = int(eqn[0])
                self.equations.append(eqn)
        print(self.equations)
        
    def problem1(self):
        sol = 0
        for equation in self.equations:
            if self.op(len(equation[1]) - 1, equation[0], equation[1]):
                sol += equation[0]
        print(sol)
    
    def problem2(self):
        sol = 0
        for equation in self.equations:
            if self.op1(0, equation[1][0], equation[0], equation[1]):
                sol += equation[0]
        print(sol)
    
    def op1(self, index, val, finalValue, arr):
        if index == len(arr) -1:
            if val == finalValue:
                return True
            else:
                return False
        concat = self.op1(index + 1, int(str(val) + str(arr[index + 1])), finalValue, arr)
        mul = self.op1(index + 1, val * arr[index + 1], finalValue, arr)
        add = self.op1(index + 1, val + arr[index + 1], finalValue, arr)
        return concat or mul or add
        
        
    def op(self, index, val, arr):
        if index == 0:
            if val == arr[index]:
                return True
            else: 
                return False
        mul = self.op(index - 1, val/ arr[index], arr)
        add = self.op(index - 1, val - arr[index], arr)

        return mul or add

if __name__ == "__main__":#
    if len(sys.argv) != 2:
        print("Usage: python prob1.py <filename>")
    else:
        filename = sys.argv[1]
        problem = Problem(filename)
        problem.problem2()