class Solution:
    def fractionToDecimal(self, numerator, denominator):
        fin1 = str(numerator // denominator)
        ans = numerator % denominator
        res = " "
        sample = {}
        while ans != 0 and ans not in sample:
            sample[ans] = len(res)
            ans = ans * 10
            ans_part = ans // denominator
            res += str(ans_part)
            ans = ans % denominator
        if ans == 0:
            c1 = numerator / denominator
            if c1 % 1 == 0:
                return str(int(c1))
            else:
                return str(c1)

        else:
            return fin1 + "." + res[: sample[ans]] + "(" + res[sample[ans] :] + ")"


S = Solution()
print(S.fractionToDecimal(23, 3))
