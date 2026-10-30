"""
Reverse Linked List (Easy)

You're given the head of a singly linked list. Reverse the list so every link points the other way, and return the new head. In the examples, a list is written as its values in order.

Example 1:
Input: head = [0, 1, 2, 3]
Output: [3, 2, 1, 0]
Explanation: The last node becomes the new head.

Example 2:
Input: head = [1]
Output: [1]
Explanation: One node stays as it is.

Example 3:
Input: head = []
Output: []
Explanation: An empty list has head None, and you should return None.

Constraints:
- 0 <= number of nodes <= 1,000
- -1,000 <= Node.val <= 1,000
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: "ListNode | None") -> "ListNode | None":
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
