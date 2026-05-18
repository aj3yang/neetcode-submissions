class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums.sort()
        freq = {}
        ans = []

        arr = []
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        for key, val in freq.items():
            arr.append([val, key])
        arr.sort()

        for i in range(k):
            v = arr.pop()[1]
            ans.append(v)

    
        return ans