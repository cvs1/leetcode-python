class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return len(bin(n)[2:].replace("0", "")) == 1


Solution().isPowerOfTwo(16)
