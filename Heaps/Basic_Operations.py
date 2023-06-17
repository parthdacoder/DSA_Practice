class Heap:
    def __init__(self):
        self.heap = [0]
        
    def push(self,val):
        self.heap.append(val)
        i = len(self.heap) - 1
        
        while self.heap[i] < self.heap[i//2]:
            print(self.heap[i])
            tmp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = tmp
            i = i//2
            
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
            
        res = self.heap[1]
        
        
# Create a heap instance
heap = Heap()

# Push values onto the heap
heap.push(5)
heap.push(3)
heap.push(8)
heap.push(1)
heap.push(10)

# Print the heap
# print(heap.heap)

