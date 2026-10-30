"""
Reconstruct Itinerary (Hard)

tickets lists flights as [from, to]. Starting from "JFK", use every ticket exactly once. If several routes work, return the one that comes first alphabetically when compared as a list. At least one valid route exists.

Example 1:
Input: tickets = [["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]]
Output: ["JFK", "BUF", "HOU", "SEA"]

Example 2:
Input: tickets = [["HOU", "JFK"], ["SEA", "JFK"], ["JFK", "SEA"], ["JFK", "HOU"]]
Output: ["JFK", "HOU", "JFK", "SEA", "JFK"]
Explanation: HOU comes before SEA alphabetically.

Example 3:
Input: tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
Output: ["JFK", "NRT", "JFK", "KUL"]
Explanation: Going to KUL first would leave you stuck with unused tickets.

Constraints:
- 1 <= len(tickets) <= 300
"""

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
