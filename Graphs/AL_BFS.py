from collections import deque

def bfs(node, target, adjList):
    length = 0
    visit = set()
    queue = deque()
    queue.append(node)
    
    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length
            
            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
        
    return length

adjList = {
    "A": ["B"],
    "B": ["C", "E"],
    "C": ["E"],
    "E": ["D"],
    "D": []
}

print(bfs("A", "E", adjList) )