class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data == None:
            self.data = data

        else:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


def inOrderPrint(root):
    if root is None:
        return None
    else:
        inOrderPrint(root.left)
        print(root.data, end=" ")
        inOrderPrint(root.right)


def preOrderPrint(root):
    if root is None:
        return
    else:
        print(root.data, end=' ')
        preOrderPrint(root.left)
        preOrderPrint(root.right)


def postOrderPrint(root):
    if root is None:
        return
    else:
        postOrderPrint(root.left)
        postOrderPrint(root.right)
        print(root.data, end=' ')


if __name__ == '__main__':
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')


# inOrderPrint(root)
# preOrderPrint(root)
postOrderPrint(root)
