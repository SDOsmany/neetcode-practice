"""
Walls And Gates (Medium)

rooms is a grid where -1 is a wall, 0 is a gate and 2147483647 is an empty room. Fill each empty room with its distance to the nearest gate, moving up, down, left or right. Leave a room unchanged if no gate can be reached. Change rooms in place and return nothing.

Example 1:
Input: rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
Output: [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
Explanation: Every empty room gets its distance to the closer of the two gates.

Example 2:
Input: rooms = [[0, -1], [2147483647, 2147483647]]
Output: [[0, -1], [1, 2]]

Example 3:
Input: rooms = [[2147483647, -1, 0]]
Output: [[2147483647, -1, 0]]
Explanation: The wall blocks the room from the gate.

Constraints:
- 1 <= rows, columns <= 100
"""

from collections import deque

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        q = deque((r, c) for r, row in enumerate(rooms) for c, v in enumerate(row) if v == 0)
        while q:
            r, c = q.popleft()
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]) and rooms[x][y] == 2147483647:
                    rooms[x][y] = rooms[r][c] + 1
                    q.append((x, y))


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
