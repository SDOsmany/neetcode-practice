
def check(mod, eq):
    s = mod.Solution()
    eq(s.findItinerary(tickets=[["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]]), ["JFK", "BUF", "HOU", "SEA"])
    eq(s.findItinerary(tickets=[["HOU", "JFK"], ["SEA", "JFK"], ["JFK", "SEA"], ["JFK", "HOU"]]), ["JFK", "HOU", "JFK", "SEA", "JFK"])
    eq(s.findItinerary(tickets=[["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]), ["JFK", "NRT", "JFK", "KUL"])
