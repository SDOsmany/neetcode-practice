"""
Pow(x, n) (Medium)

Return x raised to the power n, without using ** or a built-in power function. n can be negative or 0. Your solution should run in O(log n) time.

Example 1:
s.myPow(2.0, 5)  ->  32.0

Example 2:
s.myPow(1.1, 10)  ->  about 2.59374
Explanation: Tests compare to 5 decimal places.

Example 3:
s.myPow(2.0, -3)  ->  0.125
Explanation: A negative power means one over the positive power.

Constraints:
- -100 < x < 100
- -1,000 <= n <= 1,000,000
- If n is negative, x isn't 0
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
