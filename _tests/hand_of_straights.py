
def check(mod, eq):
    s = mod.Solution()
    eq(s.isNStraightHand(hand=[1, 2, 4, 2, 3, 5, 3, 4], groupSize=4), True)
    eq(s.isNStraightHand(hand=[1, 2, 3, 3, 4, 5, 6, 7], groupSize=4), False)
    eq(s.isNStraightHand(hand=[1, 2, 3], groupSize=2), False)
