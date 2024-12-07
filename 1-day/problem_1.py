prevL = 0
prevR = 0
lCount = -1
rCount = -1
index = 0
left = []
right = []
with open("input1.txt") as fileIn:
    for line in fileIn:
        l, r = (int(s) for s in line.split())
        left.append(l)
        right.append(r)


sol = sum([left[i] * right.count(left[i]) for i in range(len(left))])

print(sol)
        