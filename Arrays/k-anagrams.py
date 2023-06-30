from collections import *


class Solution:
    def areKAnagrams(self, str1, str2, k):
        if len(str1) != len(str2):
            return False

        a1 = Counter(str1)
        a2 = Counter(str2)
        count = 0

        for key in a1:
            diff = a1[key] - a2.get(key, 0)
            if diff > 0:
                count += diff

        if count <= k:
            return True

        return False
