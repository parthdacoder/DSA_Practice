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

    def printNthFromLast(self, n):
        curr = self.head
        a = len(llist)
        pos = 0
        len_from_start = a-n
        # print(len_from_start)
        while curr != None:
            if pos == len_from_start:
                print(curr.data)
            curr = curr.next
            pos = pos+1


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
llist.printList()
llist.printNthFromLast(3)
