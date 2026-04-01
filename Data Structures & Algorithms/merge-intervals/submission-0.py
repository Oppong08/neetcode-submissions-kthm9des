class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        merged = [intervals[0]]
        for start, end in intervals[1:]:

            if start <= merged[-1][1]: #if the start of one event is withing the end time of the most recently merged event, merged them
                merged[-1][1] = max(end,merged[-1][1])

            else:
                merged.append([start, end])
        
        return merged
    