from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(1)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_pt = last_pt = -1
        min_dist = float('inf')

        prev = head
        curr = head.next
        index = 1

        while curr.next:
            next_node = curr.next
            if (curr.val > prev.val and curr.val > next_node.val) or (curr.val < prev.val and curr.val < next_node.val):
                if first_pt == -1:
                    first_pt = index
                else:
                    min_dist = min(min_dist, index - last_pt)
                last_pt = index

            prev = curr
            curr = next_node
            index += 1

        if first_pt == last_pt:
            return [-1, -1]

        return [min_dist, last_pt - first_pt]

# Instantiate Solution and call the method
solution = Solution()
result = solution.nodesBetweenCriticalPoints(node1)
print(result)
