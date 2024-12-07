count = 0
with open("input2.txt") as fileIn:
    for line in fileIn:
        valid = True
        arr = [int(s) for s in line.split()]
        increasing = arr[1] - arr[0] >= 1
        for i in range(len(arr) - 1):
            if increasing:
                diff = arr[i+1] - arr[i]
                if not (diff >= 1 and diff <= 3):
                    valid = False
                    break
            else:
                diff = arr[i + 1] - arr[i]
                if not (diff <= -1 and diff >= -3):
                    valid = False
                    break
        if valid:
            count += 1
print(count)
            