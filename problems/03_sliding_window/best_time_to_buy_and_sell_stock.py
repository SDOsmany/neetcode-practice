"""
Best Time to Buy And Sell Stock (Easy)

prices[i] is a stock's price on day i. You may buy once and sell once, and the sale must be on a later day than the purchase. Return the largest profit you can make. If no trade makes money, return 0.

Example 1:
Input: prices = [10, 1, 5, 6, 7, 1]
Output: 6
Explanation: Buy on day 1 at price 1 and sell on day 4 at price 7.

Example 2:
Input: prices = [10, 8, 7, 5, 2]
Output: 0
Explanation: Prices only fall, so the best choice is not to trade.

Example 3:
Input: prices = [2, 4, 1, 3]
Output: 2
Explanation: Buying at 2 and selling at 4, or buying at 1 and selling at 3, both earn 2.

Constraints:
- 1 <= len(prices) <= 100
- 0 <= prices[i] <= 100
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
