class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}

        for i in t:
            if i in t_map:
                t_map[i] += 1
            else:
                t_map[i] = 1

        left = 0
        have = 0
        need = len(t_map)

        res = [-1, -1]
        res_len = float("inf")

        window_map = {}

        for right in range(len(s)):
            if s[right] in window_map:
                window_map[s[right]] += 1
            else:
                window_map[s[right]] = 1

            if s[right] in t_map and window_map[s[right]] == t_map[s[right]]:
                have += 1

            while have == need:
                if right-left+1 < res_len:
                    res = [left, right]
                    res_len = right-left+1

            
                window_map[s[left]] -= 1

                if s[left] in t_map and window_map[s[left]] < t_map[s[left]]:
                    have -= 1

                left += 1

        if res_len == float('inf'):
            return ""
        else:
            return s[res[0]:res[1]+1]
        