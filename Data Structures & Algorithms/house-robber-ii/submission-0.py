class Solution:
    def rob(self, nums: List[int]) -> int:
        first_dp = []
        second_dp = []

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        first_dp.append(nums[0])
        first_dp.append(max(nums[0], nums[1]))

        second_dp.append(nums[1])
        second_dp.append(max(nums[1], nums[2]))

        #alt = nums[1:]

        for i in range(2, len(nums)-1):
            first_dp.append(max(first_dp[i-1], first_dp[i-2] + nums[i]))

        for i in range(3, len(nums)):
            second_dp.append(max(second_dp[i-2], second_dp[i-3] + nums[i]))

        return max(first_dp[-1], second_dp[-1])