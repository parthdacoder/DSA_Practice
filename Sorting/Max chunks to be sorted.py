class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = 0
        mx = 0
        for i, x in enumerate(arr):
            mx = max(mx, x)
            if mx == i:
                ans += 1
        return ans


nums = [1, 0, 3, 2, 4, 5]
obj = Solution()
print(obj.maxChunksToSorted(nums))
