"""
Reorder List (Medium)

Rearrange a linked list L0, L1, ..., Ln into L0, Ln, L1, Ln-1, L2, ... by relinking nodes, without changing their values. Change the list in place and return nothing.

Example 1:
Input: head = [2, 4, 6, 8]
Output: [2, 8, 4, 6]
Explanation: Take from the front, then the back, alternately.

Example 2:
Input: head = [2, 4, 6, 8, 10]
Output: [2, 10, 4, 8, 6]

Example 3:
Input: head = [1, 2]
Output: [1, 2]

Constraints:
- 1 <= number of nodes <= 1,000
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: "ListNode | None") -> None:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            second.next, prev, second = prev, second, second.next
        first = head
        while prev:
            first.next, prev.next, first, prev = prev, first.next, first.next, prev.next


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
