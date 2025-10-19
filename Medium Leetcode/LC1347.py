class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = {}
        t_freq = {}

        for ch in s:
            s_freq[ch] = s_freq.get(ch, 0) + 1
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1

        common_cnt = 0
        for key in s_freq.keys():
            if t_freq.get(key, 0) >= s_freq.get(key):
                common_cnt += s_freq.get(key)
            elif t_freq.get(key):
                common_cnt += t_freq.get(key)

        return len(s) - common_cnt


s = "leetcode"
t = "practice"
print(Solution().minSteps(s, t))
