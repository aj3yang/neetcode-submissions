class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0

        max_count = 0
        ans = 0
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1

            max_count = max(max_count, freq[s[r]])

            if (r - l + 1) - k > max_count:
                freq[s[l]] -= 1
                l += 1

            ans = max(ans, r-l+1)

        return ans


