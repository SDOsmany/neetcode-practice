
def check(mod, eq):
    s = mod.Solution()
    eq(s.canFinish(numCourses=2, prerequisites=[[0, 1]]), True)
    eq(s.canFinish(numCourses=2, prerequisites=[[0, 1], [1, 0]]), False)
    eq(s.canFinish(numCourses=3, prerequisites=[]), True)
