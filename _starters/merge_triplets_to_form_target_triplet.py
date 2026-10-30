"""
Merge Triplets to Form Target Triplet (Medium)

You can repeatedly pick two triplets and replace one with their position-by-position maximum. Return True if you can make target appear.

Example 1:
Input: triplets = [[1, 2, 3], [7, 1, 1]], target = [7, 2, 3]
Output: True
Explanation: Merging both gives [7, 2, 3].

Example 2:
Input: triplets = [[2, 5, 6], [1, 4, 4], [5, 7, 5]], target = [5, 4, 6]
Output: False
Explanation: Each triplet that could help has a value too large.

Example 3:
Input: triplets = [[1, 1, 1]], target = [1, 1, 1]
Output: True

Constraints:
- 1 <= len(triplets) <= 1,000
"""

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
