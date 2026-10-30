"""
Clone Graph (Medium)

You're given one node of a connected undirected graph. Each Node has a val and a list of neighbors. Return a deep copy of the entire graph: brand-new Node objects with the same values and the same connections. No node in the copy may be an original node. If the input is None, return None.

Example 1:
Input: node 1 connected to 2, node 2 connected to 1 and 3, node 3 connected to 2; start at node 1
Output: a new node 1 with the same shape
Explanation: Each new node's neighbors must be new nodes too.

Example 2:
Input: node 5 with no neighbors
Output: a new node 5 with no neighbors
Explanation: One node with nothing connected.

Example 3:
Input: node = None
Output: None
Explanation: An empty graph.

Constraints:
- 0 <= number of nodes <= 100
- Node values are unique
- The graph may contain cycles
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node | None") -> "Node | None":
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
