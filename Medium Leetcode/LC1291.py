from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        all_combinations, ans = [], []
        ans = []
        for i in range(1, 10):
            for j in range(0, 10 - i):
                all_combinations.append(int(digits[j:j + i]))

        for i in range(0, len(all_combinations)):
            if all_combinations[i] >= low and all_combinations[i] <= high:
                ans.append(all_combinations[i])

        return ans


print(Solution().sequentialDigits(1000, 13000))
