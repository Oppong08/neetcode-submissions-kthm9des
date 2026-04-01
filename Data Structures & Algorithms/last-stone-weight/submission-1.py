class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #sorting:
        while len(stones)>1:
            stones.sort()

            first, second = stones.pop(), stones.pop()
            if (first > second) or (second > first):
                curr = abs(first - second)
                stones.append(curr)
        
        return stones[0] if stones else 0


      #use max heap, pop out the twe largest stones and follow steps
        # stones = [-s for s in stones]
        # heapq.heapify(stones)

        # while len(stones) > 1:
        #     first  = heapq.heappop(stones)
        #     second = heapq.heappop(stones)
        #         #  -6  -4 
        #     if second > first:
        #         heapq.heappush(stones, first - second)

        # stones.append(0)
        # return abs(stones[0])


            

       