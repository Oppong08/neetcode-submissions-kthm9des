class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = []
        intervals.sort()

        for q in queries:
            minimum = float("inf")
            for i in intervals:
                if i[0] > q:
                    break
                if i[0]<= q <= i[1]:
                    cur_range = i[1] - i[0] + 1
                    minimum = min(cur_range,minimum)
            if minimum!= float("inf"):
                output.append(minimum)
            else:
                output.append(-1)

        return output


