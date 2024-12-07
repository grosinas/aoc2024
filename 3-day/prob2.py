import re
with open("input.txt", "r") as file:
    fileContent = file.read()

donts = fileContent.split("don't()")
print(donts)
dos = []

for dont in donts:
    dos.append(dont.split("do()"))
    
print(dos)

sol = 0

beforeFirstDont = re.findall("mul\(\d+,\d+\)", donts[0])
b4firstDontSplit = [c.strip("mul(").strip(")").split(",") for  c in beforeFirstDont]
for i in range(len(b4firstDontSplit)):
    sol += int(b4firstDontSplit[i][0]) * int(b4firstDontSplit[i][1])

for i in range(1,len(dos)):
    for j in range(1,len(dos[i])):
        x = re.findall("mul\(\d+,\d+\)", dos[i][j])
        a = [c.strip("mul(").strip(")").split(",") for c in x]
        for p in range(len(a)):
            sol += int(a[p][0]) * int(a[p][1])
            
print(sol)