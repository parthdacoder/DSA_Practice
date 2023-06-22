
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        
adjList = { "A": [], "B": []}

edges = [["A","B"], ["B","C"], ["B","E"], ["C","E"], ["E","D"]]

adjList = {}

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
        
    adjList[src].append(dst)
    
for node, neighbors in adjList.items():
    print(f"Node {node} has neighbors: {neighbors}")
