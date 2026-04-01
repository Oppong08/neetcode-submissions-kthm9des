"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #two pointers
        #logic: create two sorted of arrays of all meeting start and end times
        #loop through each with two pointers, at each index s in start, if the current start time is less then the current end time e:
        #(meaning the current meeting is withing the current end time and hence overlaps with an ongoing), increase count by 1. ie. assign another room for that meeting
        #else(if the current start time is greater or equal to the current end time, meaning it doesn't overlap with an ongoing meeting, reduce count by 1) 
        #after the iteration, return the maximum count reached(maximimum overlapping meetings which amounts to the maximum rooms needed)

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        #two pointers to track ongoing meetings
        s, e = 0,0

        #initial count of rooms needed and res is the maximum number of rooms recorderd
        count, res = 0,0

        while s < len(intervals):
            #if current event overlaps with an ongoing one
            if start[s] < end[e]:
                count +=1
                s+=1
            else:
                count -= 1
                e +=1
            res = max(count, res)
        return res
