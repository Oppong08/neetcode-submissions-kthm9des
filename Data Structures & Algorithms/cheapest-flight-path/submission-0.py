class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = prices.copy()

            for s, d, p in flights: 
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices
        
        return prices[dst]


































        # #build adjacency list with node and cost
        # adj = {n: [] for i in range(n)}

        # for src,dst,cost in flights:
        #     adj[src] = [cost,dst] 

        # #set up djikstrah, set K count, if path is visited, mark as invalid
        # visit = set()
        # minH = [[0, src]]
        # cheapest = 0
        # cur = 0

        # while minH:
        #     cost, dist = heapq.heappop(minH)
        #     if cost in visit:
        #         continue
        #     if cur > k:
        #         continue
        #     if dist == dst:
        #         return cost

        #     visit.add(cost)
        #     cur += 1
            
        #     for neisrc in adj[dist]:
        #         if neisrc not in visit:
        #             heapq.heappush(minH, [cost+cheapest, neisrc])
        
            
            

            
