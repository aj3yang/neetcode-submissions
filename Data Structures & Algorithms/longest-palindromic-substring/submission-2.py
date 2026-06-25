class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr_ans = 0
        ans = ""

        for i in range(len(s)):
            curr_s = s[i]
            if (i-1 >= 0 and i+1 < len(s)):
                l_odd = i-1
                r_odd = i+1
                while (l_odd >= 0 and r_odd < len(s) and s[l_odd] == s[r_odd]):
                    curr_s = s[l_odd] + curr_s + s[r_odd]
                    l_odd -= 1
                    r_odd += 1

            if len(curr_s) > len(ans):
                ans = curr_s

            if (i+1 < len(s) and s[i] == s[i+1]):
                curr_s = s[i] + s[i+1]
                if (i-1 >= 0 and i+2 < len(s)):
                    l_even = i-1
                    r_even = i+2
                    while (l_even >= 0 and r_even < len(s) and s[l_even] == s[r_even]):
                        curr_s = s[l_even] + curr_s + s[r_even]
                        l_even -= 1
                        r_even += 1

            if len(curr_s) > len(ans):
                ans = curr_s

        return ans