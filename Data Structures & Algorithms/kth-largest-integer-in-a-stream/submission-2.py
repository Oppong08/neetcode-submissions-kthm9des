class KthLargest:

#Minheap

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap) #convert nums list to minheap
        while len(minHeap) > k: # Pop out from the heap until we have only the k largest elements in the minHeap 
            heapq.heappop(self.minHeap)

    
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
            heapq.heapop(self.minHeap)
        
        return self.minHeap[0] #return the kth largest, which for a min heap of size k would always be the first item













    #sorting
    def __init__(self, k: int, nums: List[int]):
       
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums) - self.k]