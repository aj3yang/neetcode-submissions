class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += 1
            if i-1 >= 0 and i+1 < len(s):
                l_odd = i-1
                r_odd = i+1
                while (l_odd >= 0 and r_odd < len(s) and s[l_odd] == s[r_odd]):
                    res += 1
                    l_odd -= 1
                    r_odd += 1
            
            if (i+1 < len(s) and s[i] == s[i+1]):
                res += 1
                if (i-1 >= 0 and i+2 < len(s)):
                    l_even = i-1
                    r_even = i+2
                    while (l_even >= 0 and r_even < len(s) and s[l_even] == s[r_even]):
                        res += 1
                        l_even -= 1
                        r_even += 1

        return res