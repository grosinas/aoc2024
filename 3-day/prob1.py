import re
with open("input.txt", "r") as file:
    fileContent = file.read()


x = re.findall("mul\(\d+,\d+\)", fileContent)
a = [c.strip("mul(").strip(")").split(",") for  c in x ]
print(a)
sol = 0
for i in range(len(a)):
    sol += int(a[i][0]) * int(a[i][1])

print(sol)