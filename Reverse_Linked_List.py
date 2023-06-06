class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
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

    def reverse(self):
        curr = self.head
        self.head = self.tail
        self.tail = self.head
        after = curr.next
        before = None

        for _ in range(len(L)):
            after = curr.next
            curr.next = before
            before = curr
            curr = after
        


L = LinkedList()
L.push(3)
L.push(4)
L.push(1)
L.printList()
L.reverse()
L.printList()
