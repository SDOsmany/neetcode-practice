"""
Car Fleet (Medium)

Cars drive the same way along one road toward target. position[i] and speed[i] describe car i. A car can't pass the one ahead: if it catches up, they drive together at the slower speed as one fleet. Catching up exactly at target still counts. Return how many fleets arrive.

Example 1:
Input: target = 10, position = [1, 4], speed = [3, 2]
Output: 1
Explanation: Both reach target after 3 hours, so they count as one fleet.

Example 2:
Input: target = 10, position = [4, 1, 0, 7], speed = [2, 2, 1, 1]
Output: 3
Explanation: The cars starting at 4 and 7 merge, and the other two arrive separately.

Example 3:
Input: target = 12, position = [3], speed = [3]
Output: 1

Constraints:
- 1 <= len(position) <= 1,000
- Positions are distinct and below target
- Speeds are positive
"""

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
