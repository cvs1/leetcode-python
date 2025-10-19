# 3714. Longest Balanced Substring II
# Given a string s made up of only 'a', 'b', and 'c',
# find the length of the longest substring where all distinct chars appear equally.

def longestBalancedSubstring(s: str) -> int:
    # Track counts of each character
    count = {'a': 0, 'b': 0, 'c': 0}

    # Hash map to store (diff_b_a, diff_c_a) -> first index seen
    # We initialize (0, 0) as seen at index -1 (before string starts)
    seen = {(0, 0): -1}

    maxlen = 0  # final answer

    # Loop through the string
    for i, ch in enumerate(s):
        # update counts
        count[ch] += 1

        # compute difference tuple
        diff = (count['b'] - count['a'], count['c'] - count['a'])

        # If we saw this diff before, substring between is balanced
        if diff in seen:
            # calculate length
            length = i - seen[diff]
            maxlen = max(maxlen, length)
        else:
            # store first time we see this diff
            seen[diff] = i

    return maxlen


# ------------------ TEST CASES ------------------
if __name__ == "__main__":
    tests = [
        ("abbac", 4),
        ("aabcc", 3),
        ("aba", 2),
        ("abcabc", 6),
        ("aabbcc", 6),
        ("aaaa", 1),
        ("abca", 3)
    ]

    for s, expected in tests:
        result = longestBalancedSubstring(s)
        print(f"s = {s} ➜ longest balanced = {result} (expected {expected})")
