class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
             return False
        h = {}
        for i in nums:
            if h.get(i):
                h[i] +=1
            else:
                h[i] = 1
        for j in nums:
            if h[j] > 1:
                return True
        return False
        
        