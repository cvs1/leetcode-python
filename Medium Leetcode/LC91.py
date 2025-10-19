class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0' or (len(s) >= 2 and s[len(s) - 1] == '0' and s[len(s) - 2] == '0'):
            return 0

        cnt, res, zeros = 1, 1, 0

        for i in range(0, len(s) - 1):
            if s[i] == '0':
                res = res * (cnt-2)
                cnt = 1
                continue
            if 26 >= int(s[i] + s[i + 1]) >= 10:
                cnt += 1
            else:
                res = res * cnt
                cnt = 1

        if s[-1] == '0':
            zeros += 1

        return (res * cnt) - zeros


print(Solution().numDecodings("1201234"))
