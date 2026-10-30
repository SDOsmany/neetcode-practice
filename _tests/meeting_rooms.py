
def check(mod, eq):
    s = mod.Solution()
    eq(s.canAttendMeetings(intervals=[[0, 30], [5, 10], [15, 20]]), False)
    eq(s.canAttendMeetings(intervals=[[5, 8], [9, 15]]), True)
    eq(s.canAttendMeetings(intervals=[[1, 2], [2, 3]]), True)
