"""
Merge Two Sorted Lists (Easy)

You're given the heads of two linked lists, each sorted in ascending order. Join them into one sorted list by relinking the existing nodes, and return its head.

Example 1:
Input: list1 = [1, 2, 4], list2 = [1, 3, 5]
Output: [1, 1, 2, 3, 4, 5]
Explanation: At each step, the smaller of the two front values goes next.

Example 2:
Input: list1 = [], list2 = [1, 2]
Output: [1, 2]
Explanation: If one list is empty, the answer is the other list.

Example 3:
Input: list1 = [], list2 = []
Output: []
Explanation: Both empty means the result is None.

Constraints:
- 0 <= number of nodes in each list <= 100
- Both lists are sorted in ascending order
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: "ListNode | None", list2: "ListNode | None") -> "ListNode | None":
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
