class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        min_operations = 0
        cnt = 1


        for ind in range(1, len(word)):
            if word[ind] == word[ind - 1] or ord(word[ind]) == ord(word[ind - 1]) + 1 or ord(word[ind]) == ord(word[ind - 1]) - 1:
                cnt += 1
            elif cnt >= 2:
                min_operations += cnt // 2
                cnt = 1

        return min_operations + (cnt//2)


obj = Solution()
print(obj.removeAlmostEqualCharacters("abcdefg"))
