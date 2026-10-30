"""
Network Delay Time (Medium)

There are n nodes labeled from 1. Each item in times is [u, v, t]: a signal takes t time to travel from u to v, in that direction only. A signal starts at node k. Return how long until every node has received it, or -1 if some node never does.

Example 1:
Input: times = [[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]], n = 4, k = 1
Output: 3
Explanation: The path 1 -> 2 -> 3 -> 4 reaches node 4 at time 3.

Example 2:
Input: times = [[1, 2, 1], [2, 3, 1]], n = 3, k = 2
Output: -1
Explanation: Node 1 can't be reached from node 2.

Example 3:
Input: times = [[1, 2, 5]], n = 2, k = 1
Output: 5

Constraints:
- 1 <= k <= n <= 100
- 1 <= t <= 100
"""

import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = {}
        for u, v, t in times:
            adj.setdefault(u, []).append((v, t))
        dist = {}
        heap = [(0, k)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = d
            for v, t in adj.get(u, []):
                if v not in dist:
                    heapq.heappush(heap, (d + t, v))
        return max(dist.values()) if len(dist) == n else -1


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
