class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        #O(1)
        #key logic:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
            if len(count) <= 2:
                continue

            for n, c in count.items():
                count[n] -= 1

            new_count = defaultdict(int)
            for n,c in count.items():
                if c > 1:
                    new_count[n] = c-1
            
            count = new_count

        res = []
        for n in count:
            if nums.count(n) > len(nums)//3:
                res.append(n)
        return res










        # n = len(nums)
        # res = set()
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num,0)
        #     if count[num] > n/3:
        #         res.add(num) 
        # return list(res)
