class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1

    def printList(self):
        curr = self.head
        while curr != None:
            print(str(curr.data)+"->", end='')
            curr = curr.next
        print('NULL')

    