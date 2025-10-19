from typing import List
import collections

class Solution:
    def costliestPath(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int, parent: int) -> int:
            max_child_cost = 0
            is_leaf = True

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                is_leaf = False
                max_child_cost = max(max_child_cost, dfs(neighbor, node))

            return cost[node] + (0 if is_leaf else max_child_cost)

        return dfs(0, -1)

n = 5
edges = [[0,1],[1,2],[1,3],[3,4]]
cost = [1, 2, 3, 4, 5]

sol = Solution()
print(sol.costliestPath(n, edges, cost))  # Output: 12 (path 0→1→3→4)
