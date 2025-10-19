class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left_most = t.rindex(s[0], 0, len(t) - 1)


