import heapq
def intersection(list1, list2):
    return [i for i in list1 if i in list2]

# Topological sort of incorrect nodes
def topologicalSort(nodes, pred, anc):
    result = []
    pq = [node for node in nodes if pred.get(node) == 0]
    
    while pq:
        current = pq.pop(0)
        result.append(current)
        
        for neighbor in anc.get(current):
            pred[neighbor] = pred.get(neighbor) - 1
            if pred.get(neighbor) == 0:
                pq.append(neighbor)
    return result
    
rules = []  
updates = []
adjList = {}
with open("input.txt") as fileIn:
    for line in fileIn:
        line = line.strip()
        if "|" in str(line):
            rule = line.split("|")
            rules.append(rule)
        else:
            update = str(line).split(",")
            updates.append(update)
##print(rules)
##print(updates)
sol = []
ruleSet = {}
for rule in rules:
    ruleSet[rule[1]] = ruleSet.get(rule[1], []) + [rule[0]]
    adjList[rule[0]] = adjList.get(rule[0],[]) + [rule[1]]
    #print(rule[0], adjList.get(rule[0]))

# for key in ruleSet.keys():
#     #print(key, ruleSet.get(key))

# finding incorrect updates
for update in updates[1:]:
    prev = []
    correct = True
    for item in update:
        prev.append(item)
        for restriction in ruleSet.get(item, []):
            if restriction in update:
                ##print(restriction, prev)
                if restriction not in prev:
                    correct = False
                    sol.append(update)
                    break
        if not correct:
            break

##print(sol)
newAdjList = []
#print(intersection(adjList.get("47"), sol[2]))
ans = []
# get adjancy list and number of predecesors for each update
for nodes in sol:
    anc = {}
    pred = {}
    for item in nodes:
        anc[item] = intersection(adjList.get(item, []), nodes)
        pred[item] = len(intersection(ruleSet.get(item,[]), nodes))
        #print(item, adj.get(item))
    
    
    print(anc)
    print(pred)
    #print(topologicalSort(nodes, pred, anc))
    ans.append(topologicalSort(nodes, pred, anc))
    
    

mids = 0
for item in ans:
    mids += int(item[len(item)//2])
        
print(mids)