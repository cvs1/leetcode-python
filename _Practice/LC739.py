from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        stack = [len(temperatures) - 1]

        for i in range(len(temperatures) - 2, -1, -1):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                stack.pop()
            if stack and temperatures[stack[-1]] > temperatures[i]:
                output[i] = stack[-1] - i
                stack.append(i)

            if not stack:
                stack.append(i)

        return output


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
