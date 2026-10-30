"""
Number of Connected Components In An Undirected Graph (Medium)

There are n nodes labeled from 0, and edges lists undirected connections. Return how many separate connected groups there are.

Example 1:
Input: n = 3, edges = [[0, 1], [0, 2]]
Output: 1

Example 2:
Input: n = 6, edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
Output: 2
Explanation: 0 to 3 form one group, and 4 and 5 form another.

Example 3:
Input: n = 3, edges = []
Output: 3

Constraints:
- 1 <= n <= 1,000
"""

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
