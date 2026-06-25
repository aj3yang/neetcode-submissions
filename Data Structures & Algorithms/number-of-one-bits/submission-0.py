class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        for i in range(32):
            comp = 1 << i

            if (n & comp > 0):
                ans += 1

        return ans