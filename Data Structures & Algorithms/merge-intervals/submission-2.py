class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key = lambda x:x[0])

        # merged = [intervals[0]]
        # for start, end in intervals[1:]:
        #     if start <= merged[-1][1]: #if the start of one event is withing the end time of the most recently merged event, merged them
        #         merged[-1][1] = max(end,merged[-1][1])

        #     else:
        #         merged.append([start, end])
        
        # return merged

        intervals.sort()
        res = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= res[-1][1]:
                res[-1] = [min(res[-1][0],i[0]), max(res[-1][1], i[1])]
            else:
                res.append(i)
        return res