class Solution:
    def smallestPalindrome(self, s: str) -> str:

        characters = []
        nor, res = "", ""

        for ch in range(0, len(s) // 2):
            characters.append(s[ch])

        characters.sort()

        for ch in characters:
            nor += ch


        if len(s) % 2 == 1:
            res = nor + s[(len(s) // 2)]
        else:
            res = nor

        for ch in reversed(characters):
            res += ch

        return res


print(Solution().smallestPalindrome("daccad"))
