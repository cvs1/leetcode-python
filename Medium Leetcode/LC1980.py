from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        num_int = []
        for num in nums:
            num_int.append(int(num, 2))

        num_int.sort()

        for i in range(0, len(num_int)):
            if i != num_int[i]:
                return "0" * (len(nums) - len(bin(i)[2::])) + bin(i)[2::]

        return "1" * len(nums)


nums = ["0000000111", "0000001001", "0000000100", "0000000001", "0000000010", "1111111111", "0000000101", "0000000000",
        "0000001000", "0000000110"]
print(Solution().findDifferentBinaryString(nums))
