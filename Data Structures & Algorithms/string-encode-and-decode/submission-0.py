class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            n = len(i)
            n = str(n)
            s = s + n
            s = s + '#'
            s = s + i
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        n_str = ""
        while (i < len(s)):
            #print(n_str)
            if s[i] == '#':
                #print(n_str)
                n = int(n_str)
                #print(n)
                new_s = ""
                for j in range(1, n+1):
                    new_s = new_s + s[i+j]
                #print(new_s)
                n_str = ""
                i = i + n + 1
                res.append(new_s)
            else:
                n_str = n_str + s[i]
                i += 1

        return res