"""
Best Time to Buy And Sell Stock With Cooldown (Medium)

prices[i] is a stock's price on day i. You may trade as many times as you like, holding at most one share. After selling, you can't buy on the next day. Return the largest total profit.

Example 1:
Input: prices = [1, 3, 4, 0, 4]
Output: 6
Explanation: Buy at 1, sell at 3, wait a day, buy at 0 and sell at 4: 2 + 4 = 6.

Example 2:
Input: prices = [1]
Output: 0

Example 3:
Input: prices = [1, 2, 3, 0, 2]
Output: 3

Constraints:
- 1 <= len(prices) <= 1,000
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold, sold, rest = float("-inf"), 0, 0
        for p in prices:
            hold, sold, rest = max(hold, rest - p), hold + p, max(rest, sold)
        return max(sold, rest)


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
