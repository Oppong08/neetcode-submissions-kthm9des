class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


      #use max heap, pop out the twe largest stones and follow steps
   
        # stones = [-s for s in stones]
        # heapq.heapify(stones)

        # while len(stones) > 1:
        #     first = heapq.heappop(stones)
        #     second = heapq.heappop(stones)
        #     if second > first:
        #         heapq.heappush(stones, first - second)

        # stones.append(0)
        # return abs(stones[0])
   

   
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first  = heapq.heappop(stones)
            second = heapq.heappop(stones)
                #  -6  -4 
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])


            

       