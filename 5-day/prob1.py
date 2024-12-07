rules = []
updates = []
with open("input.txt") as fileIn:
    for line in fileIn:
        line = line.strip()
        if "|" in str(line):
            rule = line.split("|")
            rules.append(rule)
        else:
            update = str(line).split(",")
            updates.append(update)
#print(rules)
#print(updates)
sol = []
ruleSet = {}
for rule in rules:
    ruleSet[rule[1]] = ruleSet.get(rule[1], []) + [rule[0]]
    
def intersection(list1, list2):
    return [i for i in list1 if i in list2]
# for key in ruleSet.keys():
#     print(key, ruleSet.get(key))
for update in updates[1:]:
    prev = []
    correct = True
    for item in update:
        prev.append(item)
        for restriction in ruleSet.get(item, []):
            if restriction in update:
                #print(restriction, prev)
                if restriction not in prev:
                    correct = False
                    break
        if not correct:
            break
    if correct:
        sol.append(update)
    
mids = 0
for item in sol:
    mids += int(item[len(item)//2])
        
print(mids)