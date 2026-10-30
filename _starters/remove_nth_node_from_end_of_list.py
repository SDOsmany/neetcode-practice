"""
Remove Nth Node From End of List (Medium)

Remove the nth node from the end of a linked list and return the new head.

Example 1:
Input: head = [1, 2, 3, 4], n = 2
Output: [1, 2, 4]
Explanation: The second node from the end holds 3.

Example 2:
Input: head = [5], n = 1
Output: []

Example 3:
Input: head = [1, 2], n = 2
Output: [2]
Explanation: Removing the first node changes the head.

Constraints:
- 1 <= n <= number of nodes <= 100
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: "ListNode | None", n: int) -> "ListNode | None":
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
