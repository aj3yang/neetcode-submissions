class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s1) > len(s2):
            return False

        fmap1 = [0] * 26
        for i in s1:
            c = ord(i)-97
            fmap1[c] += 1
        i = 0
        while i <= len(s2) - len(s1):
            fmap2 = [0] * 26

            for j in s2[i:i+len(s1)]:
                c = ord(j) - 97
                fmap2[c] += 1
            
            if fmap1 == fmap2:
                return True
            i += 1

        return False
            



