class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = float('-inf')
        current_max = 1
        current_min = 1

        for i in range(len(nums)):
            temp = current_max * nums[i]
            current_max = max(nums[i], temp, nums[i] * current_min)
            #print("Current max: " + str(current_max))
            current_min = min(nums[i], nums[i] * current_min, temp)
            #print("Current min: " + str(current_min))

            max_so_far = max(max_so_far, current_max)

        return max_so_far