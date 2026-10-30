"""
Reverse Nodes In K Group (Hard)

Reverse the nodes of a linked list k at a time and return the new head. If fewer than k nodes remain at the end, leave them in their original order. Relink nodes rather than changing values.

Example 1:
Input: head = [1, 2, 3, 4, 5, 6], k = 3
Output: [3, 2, 1, 6, 5, 4]
Explanation: Both groups of three are reversed.

Example 2:
Input: head = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]
Explanation: The last two nodes don't form a full group.

Example 3:
Input: head = [1, 2], k = 1
Output: [1, 2]

Constraints:
- 1 <= k <= number of nodes <= 100
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: "ListNode | None", k: int) -> "ListNode | None":
        dummy = before = ListNode(0, head)
        while True:
            end = before
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next
            after = end.next
            prev, cur = after, before.next
            while cur is not after:
                cur.next, prev, cur = prev, cur, cur.next
            first = before.next
            before.next = end
            before = first


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
