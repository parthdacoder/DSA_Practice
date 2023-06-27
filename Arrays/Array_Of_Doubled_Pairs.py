from collections import Counter


class Solution:
    def canReorderDoubled(self, arr):
        n = [a for a in arr if a < 0]
        p = [a for a in arr if a >= 0]
        arr = sorted(n, reverse=True) + sorted(p)

        c = Counter(arr)

        for a in arr:
            if c[a] == 0:
                continue

            if c[2 * a] == 0:
                return False

            c[a] -= 1
            c[2 * a] -= 1

        return True


s = Solution()
print(s.canReorderDoubled([4, -2, 2, -4]))
