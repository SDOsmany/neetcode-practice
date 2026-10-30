"""
Gas Station (Medium)

Gas stations sit on a circular route. gas[i] is the fuel at station i, and cost[i] is the fuel needed to reach the next one. Starting with an empty tank, return the index of the station you can start from to complete the loop, or -1 if none works. If an answer exists, it's unique.

Example 1:
Input: gas = [1, 2, 3, 4], cost = [2, 2, 4, 1]
Output: 3
Explanation: Start at index 3 with 4 fuel, and the tank never goes negative.

Example 2:
Input: gas = [1, 2, 3], cost = [2, 3, 2]
Output: -1
Explanation: There isn't enough gas overall.

Example 3:
Input: gas = [5], cost = [4]
Output: 0

Constraints:
- 1 <= len(gas) == len(cost) <= 1,000
"""

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
