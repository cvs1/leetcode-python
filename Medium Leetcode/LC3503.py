import math


class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:

        return max(Solution().longestPalindromeCust(s, t), Solution().longestPalindromeCust(t, t),
                   Solution().longestPalindromeCust(s, s))

    def longestPalindromeCust(self, s: str, t: str) -> int:

        t = t[::-1]

        longest_palindrome = 0
        for i in range(0, len(s)):
            found = s[i]
            if t.find(found) != -1:
                for j in range(i + 1, len(s)):
                    found = found + s[j]
                    if t.find(found) != -1:
                        continue
                    else:
                        break

            longest_palindrome = max(longest_palindrome, len(found))

        if s == t:
            return longest_palindrome

        return (longest_palindrome - 1) * 2 + 1


s = "b"
t = "b"
max(Solution().longestPalindrome(s, t), Solution().longestPalindrome(t, t), Solution().longestPalindrome(s, s))
