class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Bruteforce: loop through for the maximum area using two for loops
        #optimal: use left and right pointers

        res = 0
        l, r = 0, len(heights) - 1
        while l < r: #width *  height since the area would depend on the minimum height 
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] < heights[r]:
                l +=1 
            # elif heights[r] < heights[l]:
            #     r -=1 
            else:
                r-=1
        return res







        # if not heights:
        #     return
        # heights.sort()
        # maxdiff = max(heights) - min(heights)
        # return maxdiff ** 2 if maxdiff else max(heights)*min(heights)
            