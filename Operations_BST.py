class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data == None:
            self.data = data

        else:
            if data < self.left:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.right:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
