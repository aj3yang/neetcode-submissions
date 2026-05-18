class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums.sort()
        m = {}
        ans = []
        freq = [[] for i in range(len(nums) + 1)]
        arr = []
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1

        for key, val in m.items():
            freq[val].append(key)

        for i in range(len(freq)- 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans