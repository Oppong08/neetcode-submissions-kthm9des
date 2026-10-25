class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #task = return k most frequent number
        #bruteforce (turns out to be the best approach): 
        #go through the array, track the frequency of each, rank them, return all ranks up to k
        #trick : use bucket sort but map count as (key) to the value of that frequency as values
        
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        ranks = [[] for i in range(len(nums) + 1)] #[[],[1],[2],[3],[],[]]

        for key,value in count.items():
            ranks[value].append(key)
        
        res = []
        for i in range(len(ranks)-1,-1, -1):
            for j in ranks[i]:
                res.append(j)
                if len(res) == k:
                    return res



        #     while k > 0:
        #         res.append(rank[i].pop())
        #         k -=1
        # return res

        #minHeap
        count = Counter(nums)

        minHeap = []

        for key,value in count:
            heapq.heappush(minHeap, [value, key])
            if lenminHeap > k:
                heapq.heappop(minHeap)
        
        return list(i for i,v in minHeap)

        


        































        # count = {}
        # freq = [[] for i in range(len(nums) + 1)] 

        # for num in nums:
        #     count[num] = 1 + count.get(num,0)

        # for i,n in count.items():
        #     freq[n].append(i)
        
        # res = []
        # for j in range(len(freq)-1,-1, -1):
        #     for m in freq[j]:
        #         res.append(m)
        #         if len(res) == k:
                    
        #             return res
        
        





















        # freq = [[] for i in range(len(nums)+1)]
        # count = {}  
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        # for i,v in count.items():
        #     freq[v].append(i)

        # res = [] #rank 
        # for i in range(len(freq)- 1, -1,-1):
        #     for j in freq[i]:
        #         res.append(j)
        #         if len(res) == k:
        #             return res















        # count = {} 
        # freq = [[] for i in range(len(nums)+1)]
        # for n in nums:  
        #     count[n] = 1 + count.get(n,0) #track the count of each item in array and puts them in count map
        
        # for n, c in count.items():
        #     freq[c].append(n) #ranks the frequencies of each item in the array(freq's index 2 is the list
        #     #of numbers that appear twice)
        
        # res = [] #tracks the k most frequent item in the array
        # for i in range(len(freq)-1,0,-1): #goes through frequencies in descending becuase the K most frequent items will be 
        # # ranked from in descending order.
        #     for j in freq[i]: #goes through the list at rank k in case there are different numbers at the rank
        #         res.append(j) #adds each item to the results
        #         if len(res) == k: #stops when we have the k most frequent items
        #             return res





 