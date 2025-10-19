class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    """Builds a binary tree from a list (like [1,2,3,None,4])."""
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


# Test cases
s = Solution()

# Example 1
p = build_tree([1, 2, 3])
q = build_tree([1, 2, 3])
print(s.isSameTree(p, q))  # ✅ True

# Example 2
p = build_tree([1, 2])
q = build_tree([1, None, 2])
print(s.isSameTree(p, q))  # ❌ False

# Example 3
p = build_tree([1, 2, 1])
q = build_tree([1, 1, 2])
print(s.isSameTree(p, q))  # ❌ False

# Custom 1 – Both empty
p = build_tree([])
q = build_tree([])
print(s.isSameTree(p, q))  # ✅ True

# Custom 2 – One empty
p = build_tree([1])
q = build_tree([])
print(s.isSameTree(p, q))  # ❌ False

# Custom 3 – Larger identical trees
p = build_tree([3, 9, 20, None, None, 15, 7])
q = build_tree([3, 9, 20, None, None, 15, 7])
print(s.isSameTree(p, q))  # ✅ True
