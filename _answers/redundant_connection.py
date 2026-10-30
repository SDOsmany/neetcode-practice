"""
Redundant Connection (Medium)

A tree with nodes numbered from 1 had one extra edge added. edges lists all the edges. Return the edge you can remove to leave a tree. If several would work, return the one that appears last in edges.

Example 1:
Input: edges = [[1, 2], [1, 3], [3, 4], [2, 4]]
Output: [2, 4]
Explanation: 1, 2, 3 and 4 form a cycle, and [2, 4] comes last.

Example 2:
Input: edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
Output: [3, 4]

Example 3:
Input: edges = [[1, 2], [2, 3], [1, 3]]
Output: [1, 3]

Constraints:
- 3 <= len(edges) <= 100
- There are no repeated edges
"""

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = list(range(len(edges) + 1))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return [a, b]
            parent[ra] = rb


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
