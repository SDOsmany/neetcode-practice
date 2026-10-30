
def check(mod, eq):
    m = mod.MedianFinder()
    m.addNum(1)
    eq(m.findMedian(), 1.0)
    m.addNum(3)
    eq(m.findMedian(), 2.0)
    m.addNum(2)
    eq(m.findMedian(), 2.0)
    m.addNum(-5)
    eq(m.findMedian(), 1.5)
