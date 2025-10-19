from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = [0] * 26

        if len(words) == 1:
            return True

        for word in words:
            for i in range(0, len(word)):
                freq[ord(word[i]) - ord('a')] += 1

        for f in freq:
            if f % len(words) != 0:
                return False

        return True


print(Solution().makeEqual(["ad"]))
