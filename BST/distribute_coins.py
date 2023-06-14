

class Solution(object):

    def distributeCoins(self, root):
        self.countMoves = 0

        def countCoinsToAncestor(root):
            if root == None:
                return 0
            if root.val > 1 and root.left is None and root.right is None:
                return root.val - 1
            leftCoins = countCoinsToAncestor(root.left)
            rightCoins = countCoinsToAncestor(root.right)
            self.countMoves += abs(leftCoins) + abs(rightCoins)
            return leftCoins + rightCoins + root.val-1

        countCoinsToAncestor(root)
        return self.countMoves
