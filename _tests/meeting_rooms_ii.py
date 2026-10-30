
def check(mod, eq):
    s = mod.Solution()
    eq(s.minMeetingRooms(intervals=[[0, 40], [5, 10], [15, 20]]), 2)
    eq(s.minMeetingRooms(intervals=[[4, 9]]), 1)
    eq(s.minMeetingRooms(intervals=[[1, 2], [2, 3]]), 1)
