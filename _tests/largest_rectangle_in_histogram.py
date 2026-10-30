
def check(mod, eq):
    s = mod.Solution()
    eq(s.largestRectangleArea(heights=[7, 1, 7, 2, 2, 4]), 8)
    eq(s.largestRectangleArea(heights=[1, 3, 7]), 7)
    eq(s.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]), 10)
