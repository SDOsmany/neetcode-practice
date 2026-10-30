"""
LRU Cache (Medium)

Design a class LRUCache with a fixed capacity. A key counts as used when you get or put it.

- LRUCache(capacity) sets the size.
- get(key) returns the value, or -1 if the key is missing.
- put(key, value) inserts or updates the key. If that goes over capacity, remove the least recently used key.

Both operations must run in O(1) time.

Example 1:
c = LRUCache(2)
c.put(1, 10)
c.get(1)  ->  10
c.put(2, 20)
c.put(3, 30)
c.get(2)  ->  20
c.get(1)  ->  -1
Explanation: When key 3 arrives, key 1 is the least recently used, because key 2 was added after it was last read.

Constraints:
- 1 <= capacity <= 100
"""

class LRUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
