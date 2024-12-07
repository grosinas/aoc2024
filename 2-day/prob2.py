def check_valid(line):
    valid = True
    l = line
    increasing = l[1] - l[0] >= 1
    for i in range(len(l) - 1):
        if increasing:
            diff = l[i+1] - l[i]
            if not (diff >= 1 and diff <= 3):
                valid = False
                break
        else:
            diff = l[i + 1] - l[i]
            if not (diff <= -1 and diff >= -3):
                valid = False
                break
    return valid

count = 0
nonValid = []
with open("input2.txt") as fileIn:
    for line in fileIn:
        valid = True
        try:
            arr = [int(s) for s in line.split(" ")]
        except:
            break
        print(arr)
        increasing = arr[1] - arr[0] >= 1
        for i in range(len(arr) - 1):
            if increasing:
                diff = arr[i+1] - arr[i]
                if not (diff >= 1 and diff <= 3):
                    valid = False
                    nonValid.append(arr)
                    break
            else:
                diff = arr[i + 1] - arr[i]
                if not (diff <= -1 and diff >= -3):
                    valid = False
                    nonValid.append(arr)
                    break
        if valid:
            count += 1
            
for line in nonValid:
    for i in range(len(line)):
        test = [line[j] for j in range(len(line)) if i != j]
        valid = check_valid(test)
        if valid:
            count += 1
            break

print(count)


