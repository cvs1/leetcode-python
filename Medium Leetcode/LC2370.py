import math
import string

from pandocfilters import Math


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        char_freq = [s.count(chr(c)) for c in range(ord('a'), ord('z') + 1)]
        max_val, frame_sum = sum(char_freq[:k]), sum(char_freq[:k])

        for j in range(k + 1, 26):
            l, r = char_freq[j - k - 1], char_freq[j]
            frame_sum = frame_sum - l + r
            # left side removed while adding right most value
            max_val = max(frame_sum, max_val)

        print(max_val)


Solution().longestIdealString("acfgbd", 2)
