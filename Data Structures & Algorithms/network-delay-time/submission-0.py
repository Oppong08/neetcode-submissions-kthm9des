class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Djitskra's Algorithm
        edges = collections.defaultdict(list)

        for u,v,w in times:
            edges[u].append((v,w))  #node -> [(neighbor, edge)]

        minHeap = [(0,k)] #stores list of (weight/cost, node)
        visit = set()
        t = 0 #result

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t,w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return t if len(visit) == n else -1 

        #time complexity: O(E * logV)