class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # l, r = 1, max(piles)
        # res = r

        # while l <= r:
        #     k = (l + r) // 2
        #     hours = 0
        #     for p in piles:
        #         hours += math.ceil(p/k)
            
        #     if hours <= h:
        #         res = min(res, k)
        #         r = k-1
        #     else:
        #         l = k + 1
        # return res
        
        #bruteforce
        k = max(piles)   #number of bananas per hour
        for i in range(1, k):
            hours = 0
            for j in range(len(piles)):
                hours += math.ceil(piles[j]/i)
            if hours <= h:
                k = min(i, k)
        return k