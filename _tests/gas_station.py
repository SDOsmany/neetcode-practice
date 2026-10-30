
def check(mod, eq):
    s = mod.Solution()
    eq(s.canCompleteCircuit(gas=[1, 2, 3, 4], cost=[2, 2, 4, 1]), 3)
    eq(s.canCompleteCircuit(gas=[1, 2, 3], cost=[2, 3, 2]), -1)
    eq(s.canCompleteCircuit(gas=[5], cost=[4]), 0)
