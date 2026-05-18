class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums.sort()
        freq = {}
        ans = []

        cnt = 1
        prev = nums[0]
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        item_list = list(sorted_freq.items())

        for i in range(k):
            ans.append(item_list[i][0])
             

            

    
        return ans