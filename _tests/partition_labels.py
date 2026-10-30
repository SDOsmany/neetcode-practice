
def check(mod, eq):
    s = mod.Solution()
    eq(s.partitionLabels(s="xyxxyzbzbbisl"), [5, 5, 1, 1, 1])
    eq(s.partitionLabels(s="abcabc"), [6])
    eq(s.partitionLabels(s="abc"), [1, 1, 1])
