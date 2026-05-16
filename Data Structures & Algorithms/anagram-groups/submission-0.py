class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        m = {}

        for i in strs:
            cfreq = [0] * 26
            for j in i:
                v = ord(j)
                cfreq[v-97] += 1
            k = tuple(cfreq)
            if k in m:
                m[k].append(i)
            else:
                m[k] = [i]

        res = []

        for key in m:
            res.append(m[key])

        return res