import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        cnt = 0
        if ladders >= len(heights):
            return len(heights) - 1

        heap = heights[0:ladders]
        heapq.heapify(heap)

        for i in range(ladders, len(heights)):
            if heights[i] <= heights[i - 1]:
                cnt += 1

            if heights[i] > heights[i - 1]:
                if len(heap) > 0 and heap[0] < heights[i] - heights[i - 1]:
                    heapq.heappushpop(heap, heights[i] - heights[i - 1])

                bricks -= (heights[i] - heights[i - 1])
                if bricks + sum(heap) < 0:
                    return cnt
                cnt += 1

        return cnt


heights = [1, 2, 4, 7, 11, 16]
print(Solution().furthestBuilding(heights, 1, 4))
