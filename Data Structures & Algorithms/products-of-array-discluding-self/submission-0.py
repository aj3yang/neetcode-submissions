class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefs = [1]
        suffs = [1]

        for i in range(len(nums)-1):
            curr = prefs[-1]
            prefs.append(curr * nums[i])
        for i in range(len(nums)-1, 0, -1):
            curr = suffs[-1]
            suffs.append(curr * nums[i])

        suffs.reverse()
        res = []
        for i in range(len(prefs)):
            res.append(prefs[i] * suffs[i])

        return res
