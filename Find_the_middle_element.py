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

    def middle(self):
        # Find out the length of index and do floor division to find middle index value
        a = (len(llist))//2
        pos = 0                 # Creat an initial pointer
        curr = self.head

        while curr != None:
            if pos == a:  # Run the loop until the middle index value matches the pointer
                # Once they match, return the data in the particular index value
                print(curr.data)
            curr = curr.next
            pos = pos + 1


if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    for i in range(5, 0, -1):
        llist.push(i)
        llist.printList()
        llist.middle()
