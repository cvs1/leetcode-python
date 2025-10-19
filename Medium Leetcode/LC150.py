from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch in ["+", "-", "/", "*"]:
                b, a = stack.pop(), stack.pop()
                if ch == "+":
                    stack.append(a + b)
                elif ch == "-":
                    stack.append(a - b)
                elif ch == "*":
                    stack.append(a * b)
                elif ch == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(ch))

        return stack[-1]


print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
