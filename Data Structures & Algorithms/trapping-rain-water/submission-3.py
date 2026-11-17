class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        cur_max = 0
        for i in range(len(height)):
            cur_max = max(cur_max, height[i])
            prefix[i] = cur_max

        cur_max = 0
        for i in range(len(height)-1, -1, -1):
            cur_max = max(cur_max, height[i])
            suffix[i] = cur_max

        for i in range(len(height)):
            ans += min(prefix[i], suffix[i]) - height[i]

        return ans
               