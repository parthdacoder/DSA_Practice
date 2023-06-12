class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Solution(object):
    def LCA(self, root, p, q):
        if root == None:
            return None

        if p.data == root.data or q.data == root.data:
            return root

        left = self.LCA(root.left, p, q)
        right = self.LCA(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        else:
            return right


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = TreeNode(2)
q = TreeNode(8)

obj = Solution()
print(obj.LCA(root, p, q).data)
