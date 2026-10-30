"""
Copy List With Random Pointer (Medium)

Each node of a linked list has a next pointer and a random pointer, which can point to any node or None. Return a deep copy: new nodes with the same values and the same next and random structure. No copied pointer may refer to an original node.

Example 1:
Values 3 -> 7, with node 3's random pointing to node 7 and node 7's random pointing to None  ->  a new list with the same shape
Explanation: The new node 3's random must point to the new node 7.

Example 2:
head = None  ->  None
Explanation: An empty list copies to an empty list.

Constraints:
- 0 <= number of nodes <= 100
"""

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node | None") -> "Node | None":
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
