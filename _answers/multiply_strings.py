"""
Multiply Strings (Medium)

num1 and num2 are non-negative integers written as strings. Return their product, also as a string. Don't convert the inputs to int all at once: the point is to multiply digit by digit, the way you would by hand.

Example 1:
Input: num1 = "3", num2 = "4"
Output: "12"
Explanation: 3 * 4 = 12.

Example 2:
Input: num1 = "111", num2 = "222"
Output: "24642"
Explanation: 111 * 222 = 24642.

Example 3:
Input: num1 = "0", num2 = "999"
Output: "0"
Explanation: The answer has no leading zeros.

Constraints:
- 1 <= len(num1), len(num2) <= 200
- Inputs contain digits only and have no leading zeros, except "0" itself
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        for i, a in enumerate(reversed(num1)):
            for j, b in enumerate(reversed(num2)):
                res[i + j] += int(a) * int(b)
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        s = "".join(map(str, reversed(res))).lstrip("0")
        return s or "0"


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
