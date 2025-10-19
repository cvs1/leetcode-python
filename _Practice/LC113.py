from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a level-order list representation."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, total):
            if not node:
                return
            path.append(node.val)
            total += node.val

            # Check if it's a leaf node with correct sum
            if not node.left and not node.right and total == targetSum:
                res.append(path[:])
            else:
                dfs(node.left, path, total)
                dfs(node.right, path, total)

            path.pop()

        dfs(root, [], 0)
        return res


# Example usage
values = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
root = build_tree(values)

sol = Solution()
print(sol.pathSum(root, 22))  # Expected: [[5, 4, 11, 2], [5, 8, 4, 5]]
