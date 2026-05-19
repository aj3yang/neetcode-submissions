class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        for i in range(len(nums)):
            n = nums[i]
            cnt = 1
            while n+1 in numSet:
                n += 1
                cnt += 1
            ans = max(ans, cnt)

        return ans
