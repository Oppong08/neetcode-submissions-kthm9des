class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #logic: add all events ending earlier than the new interval, 
        #if the next interval to be added is within new_intervals range, merge and add the new interval
        #add the remaining intervals
        # res = []
        # for i in intervals:
        #     #if first interval starts after the new_interval ends,meaning the remaining intervals do too
        #     #add the new interval and add the remaining ones
        #     if newInterval[1]< i[0]:
        #         res.append(newInterval)
        #         return res + intervals[i:]

        #     #add all intervals ending earlier than the new interval
        #     elif newInterval[0] > i[1]:
        #         res.append(i)
        #     else:
        #         newInterval = [min(i[0],newInterval[0]),max(i[1], newInterval[1])]

        #     res.append(newInterval)
        #     return res

       
        res = []
        for i in intervals:
            if i[1] < newInterval[0]:      # completely before
                res.append(i)
            elif i[0] > newInterval[1]:    # completely after
                res.append(newInterval)
                newInterval = i
            else:                           # overlap
                newInterval[0] = min(i[0], newInterval[0])
                newInterval[1] = max(i[1], newInterval[1])
        res.append(newInterval)
        return res

            
           
                


                    