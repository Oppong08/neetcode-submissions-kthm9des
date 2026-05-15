class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = set()
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
            if count[num] > n/3:
                res.add(num) 
        return list(res)
