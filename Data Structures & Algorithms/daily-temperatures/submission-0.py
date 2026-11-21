class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]
            p = (i, temp)

            while stack and stack[-1][1] < p[1]:
                res[stack[-1][0]] = p[0] - stack[-1][0]
                stack.pop()

            stack.append(p)

        return res