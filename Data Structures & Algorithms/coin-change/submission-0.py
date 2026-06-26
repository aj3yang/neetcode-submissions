class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0] * amount
        coin_set = set(coins)
        for amt in range(1, amount+1):
            if amt in coin_set:
                dp[amt-1] = 1
            else:
                min_ways = float('inf')
                for c in coins:
                    rem = amt - c
                    if rem < 0 or dp[rem-1] == 0:
                        continue
                    else:
                        min_ways = min(min_ways, 1 + dp[rem-1])

                if min_ways == float('inf'):
                    continue
                else:
                    dp[amt-1] = min_ways

        if dp[amount-1] == 0:
            return -1
        else:
            return dp[amount-1]
                    

        