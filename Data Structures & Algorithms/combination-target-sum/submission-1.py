class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(start, s, cur):
            if s == target:
                res.append(cur.copy())
                return
            for i in range(start, len(nums)):
                if s + nums[i] > target:
                    return
                #s += nums[i]
                cur.append(nums[i])
                backtrack(i, s + nums[i], cur)
                cur.pop()

        backtrack(0, 0, [])
        return res