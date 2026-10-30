"""
Graph Valid Tree (Medium)

There are n nodes labeled from 0, and edges lists undirected connections. Return True if they form a valid tree: all nodes connected and no cycles.

Example 1:
Input: n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: True

Example 2:
Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: False
Explanation: 1, 2 and 3 form a cycle.

Example 3:
Input: n = 4, edges = [[0, 1], [2, 3], [1, 0]]
Output: False
Explanation: The graph isn't all connected.

Constraints:
- 1 <= n <= 100
- Edges have no self-loops
"""

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        seen = {0}
        stack = [0]
        while stack:
            for x in adj[stack.pop()]:
                if x not in seen:
                    seen.add(x)
                    stack.append(x)
        return len(seen) == n


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
