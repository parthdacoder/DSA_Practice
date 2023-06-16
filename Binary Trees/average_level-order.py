#Solution applied easily on Level Order Traversal
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution(object):
    def levelOrderPrint(self, root):
        if root is None:
            return []
        queue = [root]
        next_queue = []
        level = []
        result = []
        answer = []
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
        # return result
        for i in result:
            sum = 0
            count = 0
            for j in range(len(i)):
                # print(i[j])
                count += 1
                sum += i[j]
            average = sum / count
            answer.append(average)
        return answer


# if __name__ == "__main__":
#     root = Node("g")
#     root.insert("c")
#     root.insert("b")
#     root.insert("a")
#     root.insert("e")
#     root.insert("d")
#     root.insert("f")
#     root.insert("i")
#     root.insert("h")
#     root.insert("j")
#     root.insert("k")
# x = Solution()
# y = x.levelOrderPrint(root)
# print(y)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

obj = Solution()
print(obj.levelOrderPrint(root))
