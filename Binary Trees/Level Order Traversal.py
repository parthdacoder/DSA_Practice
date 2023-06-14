class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        next_queue = []
        level = []
        result = []
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right != None:
                    next_queue.append(root.right)
                result.append(level)
                level = []
                queue = next_queue
                next_queue = []
            return result
