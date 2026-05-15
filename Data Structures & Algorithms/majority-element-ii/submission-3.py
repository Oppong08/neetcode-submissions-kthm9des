class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # O(n) time and O(1) space (Boyer-Moore Voting Algorithm)
        #key logic: for a given input of lenght n, the number of candidates that appear more than n/3 times will be less than 3
        #use a hash map to track candidates instead of fixed variables, hashmap shoudl allow at most 2 elements.
        #when a third element tries to enter, we decrement all counts and remove elements with count 0(non-candidate)
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
            if len(count) <= 2:
                continue

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
