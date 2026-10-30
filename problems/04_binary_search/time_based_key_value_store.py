"""
Time Based Key Value Store (Medium)

Design a class TimeMap.

- set(key, value, timestamp) stores value for key at that time. Timestamps for a key only increase.
- get(key, timestamp) returns the value set at the latest time at or before timestamp, or "" if there is none.

Example 1:
t = TimeMap()
t.set("alice", "happy", 1)
t.get("alice", 1)  ->  "happy"
t.get("alice", 2)  ->  "happy"
t.set("alice", "sad", 3)
t.get("alice", 3)  ->  "sad"
t.get("alice", 2)  ->  "happy"
Explanation: A get returns the latest value at or before its timestamp.

Constraints:
- 1 <= timestamp <= 1,000
- Keys and values are short strings
"""

class TimeMap:
    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
