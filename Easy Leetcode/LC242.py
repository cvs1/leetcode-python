class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = {}, {}

        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1

        for key in s_map.keys():
            if t_map.get(key) != s_map.get(key):
                return False

        return len(s) == len(t)


print(Solution().isAnagram("abccd", "dbcacz"))
