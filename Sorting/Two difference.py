class Solution:
    def findPair(self, arr, N):
        mapper = {}

        for num in arr:
            complement1 = num + N
            complement2 = num - N

            if complement1 in mapper or complement2 in mapper:
                return True

            mapper[num] = True
            print(mapper)

        return False


nums = [3, 1, 2, 4, 3]
obj = Solution()
print(obj.findPair(nums, 1))
