class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:

                tSum = nums[i] + nums[left] + nums[right]

                if tSum < 0:
                    left += 1
                elif tSum > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return ans