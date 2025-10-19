# Definition for a binary tree node.
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        t1_list = []

        def dfs(root: TreeNode) -> list:
            if root.left is None and root.right is None:
                t1_list.append(root.val)
                return t1_list

            dfs(root.left)
            dfs(root.right)

            return t1_list

        l1 = dfs(root1)
        t1_list = []
        l2 = dfs(root2)

        if len(l1) != len(l2): return False

        for i in range(0, len(t1_list)):
            if l1[i] != l2[i]:
                return False

        return True


root = TreeNode(1)

# Level 2
root.left = TreeNode(2)
root.right = TreeNode(3)

# Level 3
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

Solution().leafSimilar(root, root)
