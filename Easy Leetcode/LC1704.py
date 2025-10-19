class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowels_count = 0
        s = s.lower()
        for ch in s:
            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
                vowels_count += 1

        return vowels_count % 2 == 0


print(Solution().halvesAreAlike("tkPAdxpMfJiltOerItiv"))
