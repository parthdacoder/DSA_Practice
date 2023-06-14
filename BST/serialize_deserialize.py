
class Treenode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        result = []

        def dfs(node):
            if node == None:
                result.append('N')
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None
            node = Treenode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = None
root.left.right = None
root.right.left = Treenode(4)
root.right.right = Treenode(5)

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
