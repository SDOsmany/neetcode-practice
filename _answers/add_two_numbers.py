"""
Add Two Numbers (Medium)

Two non-negative integers are stored as linked lists with one digit per node, least significant digit first. Return their sum in the same form.

Example 1:
Input: l1 = [1, 2, 3], l2 = [4, 5, 6]
Output: [5, 7, 9]
Explanation: 321 + 654 = 975.

Example 2:
Input: l1 = [9], l2 = [9]
Output: [8, 1]
Explanation: 9 + 9 = 18.

Example 3:
Input: l1 = [9, 9, 9], l2 = [1]
Output: [0, 0, 0, 1]
Explanation: 999 + 1 = 1000.

Constraints:
- 1 <= number of nodes in each list <= 100
- No leading zeros, except the number 0 itself
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: "ListNode | None", l2: "ListNode | None") -> "ListNode | None":
        dummy = tail = ListNode()
        carry = 0
        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tail.next = ListNode(carry % 10)
            tail = tail.next
            carry //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
