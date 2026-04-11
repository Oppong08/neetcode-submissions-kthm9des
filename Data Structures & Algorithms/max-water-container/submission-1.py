class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Bruteforce: loop through for the maximum difference , squre it
        if not heights:
            return
        heights.sort()
        maxdiff = max(heights) - min(heights)
        return maxdiff ** 2 if maxdiff else max(heights)*min(heights)
            