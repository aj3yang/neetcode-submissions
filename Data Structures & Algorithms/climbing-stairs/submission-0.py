class Solution:
    def climbStairs(self, n: int) -> int:
        dp = []

        if n == 1:
            return 1
        if n == 2:
            return 2

        dp.append(1)
        dp.append(2)

        for i in range(2, n):
            dp.append(dp[i-2] + dp[i-1])

        return dp[-1]