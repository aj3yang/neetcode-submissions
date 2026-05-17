class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    ans.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1

        return ans