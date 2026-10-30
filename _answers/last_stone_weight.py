"""
Last Stone Weight (Easy)

stones[i] is the weight of a stone. On each turn, take the two heaviest stones, with weights x <= y, and smash them. If x == y, both are destroyed. Otherwise x is destroyed and y becomes y - x. Continue until at most one stone remains. Return its weight, or 0 if none remain.

Example 1:
Input: stones = [2, 3, 6, 2, 4]
Output: 1
Explanation: 6 and 4 leave 2, giving [2, 3, 2, 2]. 3 and 2 leave 1, giving [2, 2, 1]. 2 and 2 vanish, leaving [1].

Example 2:
Input: stones = [1, 2]
Output: 1
Explanation: 2 - 1 = 1.

Example 3:
Input: stones = [5, 5]
Output: 0
Explanation: Both stones are destroyed.

Constraints:
- 1 <= len(stones) <= 30
- 1 <= stones[i] <= 1,000
"""

import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y, x = -heapq.heappop(heap), -heapq.heappop(heap)
            if y != x:
                heapq.heappush(heap, x - y)
        return -heap[0] if heap else 0


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
