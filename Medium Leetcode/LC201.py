class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        leftstr = bin(left)[2:]
        rightstr = bin(right)[2:]

        if left == right:
            return left

        if len(leftstr) != len(rightstr):
            return 0

        changedIndex = 0

        for i in range(0, len(leftstr)):
            if leftstr[i] != rightstr[i]:
                changedIndex = i
                break

        ansBin = ""

        for j in range(0, changedIndex):
            ansBin += leftstr[j]

        ansBin = ansBin + ("0" * (len(leftstr) - len(ansBin)))

        return int(ansBin, 2)


Solution().rangeBitwiseAnd(5, 7)
