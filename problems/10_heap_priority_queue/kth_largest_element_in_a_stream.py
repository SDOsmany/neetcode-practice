"""
Kth Largest Element In a Stream (Easy)

Design a class KthLargest that tracks the kth largest value in a growing stream of numbers. Duplicates count as separate values, so this means position k in sorted order rather than the kth distinct value.

- KthLargest(k, nums) starts with the values in nums.
- add(val) inserts val and returns the current kth largest value.

Example 1:
k = KthLargest(3, [1, 2, 3, 3])
k.add(3)  ->  3
k.add(5)  ->  3
k.add(6)  ->  3
k.add(7)  ->  5
k.add(8)  ->  6
Explanation: After add(7), the values in descending order are 7, 6, 5, ..., so the third largest is 5.

Example 2:
k = KthLargest(1, [])
k.add(-3)  ->  -3
k.add(-2)  ->  -2
Explanation: nums can start empty. There will be at least k values whenever add returns.

Constraints:
- 1 <= k
- 0 <= len(nums) <= 1,000
- At least k values exist after each add
"""

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        pass

    def add(self, val: int) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
