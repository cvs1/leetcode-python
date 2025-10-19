class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        have = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c == '*':
                for j in range(26):
                    if have[j]:
                        have[j].pop()
                        break
            else:
                have[ord(c) - ord('a')].append(i)
        v = [(x, chr(i + ord('a'))) for i in range(26) for x in have[i]]
        v.sort()
        return ''.join(c for _, c in v)

Solution().clearStars("afdasf*adsfcvs**asdf*")