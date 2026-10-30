"""
Valid Palindrome (Easy)

A string counts as a palindrome here if it reads the same forwards and backwards after you remove every character that isn't a letter or digit and treat uppercase and lowercase as equal. Return True if s is a palindrome by that rule, otherwise False.

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: True
Explanation: After cleaning, it becomes "wasitacaroracatisaw", which is the same in both directions.

Example 2:
Input: s = "tab a cat"
Output: False
Explanation: After cleaning, "tabacat" reversed is "tacabat", which is different.

Example 3:
Input: s = " "
Output: True
Explanation: Nothing is left after cleaning, and an empty string counts as a palindrome.

Constraints:
- 1 <= len(s) <= 1,000
- s contains printable ASCII characters
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
