
def check(mod, eq):
    s = mod.Solution()
    norm = lambda r: sorted(r)
    eq(norm(s.pacificAtlantic(heights=[[4, 2, 7, 3, 4], [7, 4, 6, 4, 7], [6, 3, 5, 3, 6]])), norm([[0, 2], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0]]))
    eq(norm(s.pacificAtlantic(heights=[[1], [1]])), norm([[0, 0], [1, 0]]))
    eq(norm(s.pacificAtlantic(heights=[[1, 2], [4, 3]])), norm([[0, 1], [1, 0], [1, 1]]))
