import math


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

    def modular_Node(self, k):
        curr = self.head
        mod = 0
        while curr != None:
            if curr.data % k == 0:
                mod = curr.data
            curr = curr.next
        print('The Last Modular Node is', mod)


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(8)
llist.printList()
llist.modular_Node(2)
