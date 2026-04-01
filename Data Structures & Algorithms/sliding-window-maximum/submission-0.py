class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #deque:
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #remove left value from window

            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                output.append(nums[q[0]])
                l +=1
            r += 1

        return output







        # #my logic , initiate the start of every window, initiate res, for each window loop through a maximum k times calculating max
        # res = []
        # for i in range(len(nums)):
        #     max = nums[i]
        #     for j in range(i+1, k):
        #         if nums[j] > max:
        #             max = nums[j]
        #     res.append(max)
        # return res
            

