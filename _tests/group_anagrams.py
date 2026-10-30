
def check(mod, eq):
    s = mod.Solution()
    norm = lambda g: sorted(sorted(x) for x in g)
    eq(norm(s.groupAnagrams(["act","pots","tops","cat","stop","hat"])), [["act","cat"],["hat"],["pots","stop","tops"]])
    eq(norm(s.groupAnagrams(["x"])), [["x"]])
    eq(norm(s.groupAnagrams([""])), [[""]])
