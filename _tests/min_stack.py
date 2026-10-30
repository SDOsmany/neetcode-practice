
def check(mod, eq):
    m = mod.MinStack()
    m.push(1); m.push(2); m.push(0)
    eq(m.getMin(), 0)
    m.pop()
    eq(m.top(), 2)
    eq(m.getMin(), 1)
    m.push(1)
    eq(m.getMin(), 1)
    m.pop()
    eq(m.getMin(), 1)
