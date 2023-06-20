def dfs(node,target , adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)
    
    return count

adjList = {
    "A": ["B"],
    "B": ["C", "E"],
    "C": ["E"],
    "E": ["D"],
    "D": []
}

print(dfs("A", "E", adjList, set()))