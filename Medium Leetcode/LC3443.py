class Solution:
    def maxDistance(self, s: str, k: int) -> int:

        inp = s
        ans = 0
        n, e, w, s = 0, 0, 0, 0
        for ch in inp:
            if ch == 'N':
                n += 1
            if ch == 'S':
                s += 1

            if ch == 'E':
                e += 1

            if ch == 'W':
                w += 1

        common = min(n, s) + min(e, w)

        if n > min(n, s):
            ans += n - min(n, s)

        if s > min(n, s):
            ans += s - min(n, s)

        if e > min(e, w):
            ans += e - min(e, w)

        if w > min(e, w):
            ans += w - min(e, w)

        ans += min(common, k) * 2

        if common > k and inp[-2:] in {"ns", "sn", "ew", "we"}:
            ans += 1

        return ans


print(Solution().maxDistance("NSWN", 0))
