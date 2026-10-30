"""
Cheapest Flights Within K Stops (Medium)

There are n cities labeled from 0. flights[i] = [from, to, price]. Return the cheapest price from src to dst with at most k stops in between, or -1 if there's no such route.

Example 1:
Input: n = 4, flights = [[0, 1, 200], [1, 2, 100], [1, 3, 300], [2, 3, 100]], src = 0, dst = 3, k = 1
Output: 500
Explanation: With only one stop, 0 -> 1 -> 3 is the best route.

Example 2:
Input: n = 3, flights = [[1, 0, 100], [1, 2, 200], [0, 2, 100]], src = 1, dst = 2, k = 1
Output: 200

Example 3:
Input: n = 3, flights = [[0, 1, 100]], src = 0, dst = 2, k = 5
Output: -1

Constraints:
- 1 <= n <= 100
- 0 <= k < n
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
