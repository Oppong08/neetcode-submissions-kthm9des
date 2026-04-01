"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True





















        #check for overlapping 
        # intervals.sort(key=lambda i: i.start)

        # for i in range(1, len(intervals)):
        #     i1 = intervals[i - 1]
        #     i2 = intervals[i]

        #     if i1.end > i2.start:
        #         return False
        # return True
