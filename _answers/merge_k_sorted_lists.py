"""
Merge K Sorted Lists (Hard)

lists holds the heads of k sorted linked lists. Merge them into one sorted list and return its head.

Example 1:
lists = [[1, 2, 4], [1, 3, 5], [3, 6]]  ->  [1, 1, 2, 3, 3, 4, 5, 6]
Explanation: Each inner list stands for one linked list.

Example 2:
lists = []  ->  []
Explanation: No lists means an empty result.

Constraints:
- 0 <= k <= 1,000
- Each list is sorted ascending
"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list["ListNode | None"]) -> "ListNode | None":
        heap = [(n.val, i, n) for i, n in enumerate(lists) if n]
        heapq.heapify(heap)
        dummy = tail = ListNode()
        while heap:
            _, i, n = heapq.heappop(heap)
            tail.next = n
            tail = n
            if n.next:
                heapq.heappush(heap, (n.next.val, i, n.next))
        return dummy.next


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
