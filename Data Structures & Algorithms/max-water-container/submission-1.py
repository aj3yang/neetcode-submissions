class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0

        left = 0
        right = len(heights)-1
        while left < right:

            h = min(heights[left], heights[right])
            b = right - left

            ans = max(ans, h*b)

            if (heights[left] <= heights[right]):
                left += 1
            else:
                right -= 1

        return ans
