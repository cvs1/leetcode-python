from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        # Creating instances of TreeNode


        # Calling leafSimilar method
        result = Solution().leafSimilar(root1, root2)

        # Printing the result
        print(result)

        # Iterating over the generator to see the values yielded
        for value in dfs(root1):
            print(value)

root1 = TreeNode(3, TreeNode(5), TreeNode(1, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))))
root2 = TreeNode(3,
                         left=TreeNode(5),
                         right=TreeNode(1,
                                        left=TreeNode(6),
                                        right=TreeNode(2,
                                                       left=TreeNode(7),
                                                       right=TreeNode(4)
                                                       )
                                        )
                         )
Solution().leafSimilar(root1, root2)