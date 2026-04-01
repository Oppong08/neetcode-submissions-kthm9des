class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #sorting: 
        # nums.sort()
        # return nums[len(nums) - k]

        #heap

        # heapq.heapify(nums)
        # while len(nums) > k:
        #     heapq.heappop(nums)
        
        # return nums[0]

        #optimal heap: 
        #This built-in function finds the k largest elements in the list.
        #Under the hood, it uses a min-heap of size k to efficiently track the top k elements.
        #It doesn’t modify nums itself.
        return heapq.nlargest(k,nums)[-1]