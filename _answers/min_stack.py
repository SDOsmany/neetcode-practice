"""
Min Stack (Medium)

Design a class MinStack. It behaves like a normal stack but can also report its smallest value. Each of these operations must run in O(1) time:

- push(val) adds val to the top.
- pop() removes the top value.
- top() returns the top value.
- getMin() returns the smallest value currently in the stack.

Example 1:
m = MinStack()
m.push(1)
m.push(2)
m.push(0)
m.getMin()  ->  0
m.pop()
m.top()     ->  2
m.getMin()  ->  1
Explanation: After 0 is popped, the stack holds [1, 2], so the minimum goes back to 1.

Constraints:
- pop, top and getMin are only called on a non-empty stack
- Values fit in a normal integer
"""

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        low = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, low))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
