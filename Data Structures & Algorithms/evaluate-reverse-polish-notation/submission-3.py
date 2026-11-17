class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                a = stack.pop()
                b = stack.pop()
                c = 0
                if i == "+":
                    c = b + a
                if i == "-":
                    c = b - a
                if i == "*":
                    c = b * a
                if i == "/":
                    c = b / a
                stack.append(int(c))
            else:
                stack.append(int(i))

        return stack[-1]