class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #logic: sort first, loop through, keep track of previous ending of non overlaping intervals, 
        #at each index, check for overlaps, if any, increase count and choose which one to remove by updating previous ending
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            
            else:
                res+=1
                prevEnd = min(end, prevEnd)
        return res
