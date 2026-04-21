class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        minHeap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(minHeap, (r-l + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            res[q] = minHeap[0][0] if minHeap else -1
            
        return [res[q] for q in queries]


















        #bruteforce
        # output = []
        # intervals.sort()

        # for q in queries:
        #     minimum = float("inf")
        #     for i in intervals:
        #         if i[0] > q:
        #             break
        #         if i[0]<= q <= i[1]:
        #             cur_range = i[1] - i[0] + 1
        #             minimum = min(cur_range,minimum)
        #     if minimum!= float("inf"):
        #         output.append(minimum)
        #     else:
        #         output.append(-1)

        # return output




