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

    def append(self, value):
        # new_node = Node(value)
        curr = self.head
        while curr != None:
            curr = curr.next
        # curr.next = new_node

    def remove_duplicates(self):
        curr = self.head
        values = set()
        a = len(llist)
        for _ in range(a):
            values.add(curr.data)
            curr = curr.next
        # self.head = None
        for i in values:
            self.append(i)
        print(values)


llist = LinkedList()
llist.push(1)
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.printList()
llist.remove_duplicates()
llist.printList()
