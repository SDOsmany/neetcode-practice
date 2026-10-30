"""
Linked List Cycle (Easy)

You're given the head of a linked list. Return True if following next pointers from the head would eventually bring you back to a node you've already visited. Return False if the list ends at None. As a follow-up, try to use O(1) extra space.

Example 1:
Input: values 1 -> 2 -> 3 -> 4, and node 4 points back to node 2
Output: True
Explanation: After node 4 you return to node 2 and loop forever.

Example 2:
Input: values 1 -> 2, and node 2 points to None
Output: False
Explanation: The list reaches its end.

Example 3:
Input: head = None
Output: False
Explanation: An empty list can't contain a loop.

Constraints:
- 0 <= number of nodes <= 1,000
- Compare nodes by identity, not value: different nodes can hold equal values
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: "ListNode | None") -> bool:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
