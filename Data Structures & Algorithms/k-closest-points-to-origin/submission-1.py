class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #sorting: sort the list using the key = lambda and comparison parameter = (distances formula), ie:
        # points.sort(key = lambda p: p[0] ** 2 + p[1] ** 2)
        # return points[:k]


        #Minheap
        minHeap = []
        for x,y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist,x,y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        return res


        #map each point to their distances from the center, put the distances in a heap and return the k'th item
        
        # dmap = {}
        # for i in range(len(points)):
        #     x,y = points[i]
        #     d = math.sqrt(x**2 + y**2)
        #     dmap[d] = points[i]

        # mheap = heapq.heapify([dmap.values()])
        # return dmap[mheap[len(mheap-k)]]