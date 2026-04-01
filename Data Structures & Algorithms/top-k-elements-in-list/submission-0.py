class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #task = return k most frequent number
        #bruteforce (turns out to be the best approach): 
        #go through the array, track the frequency of each, rank them, return all ranks up to k
        #trick : use bucket sort but map count as (key) to the value of that frequency as values
        
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
        count = {} 
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:  
            count[n] = 1 + count.get(n,0) #track the count of each item in array and puts them in count map
        
        for n, c in count.items():
            freq[c].append(n) #ranks the frequencies of each item in the array(freq's index 2 is the list
            #of numbers that appear twice)
        
        res = [] #tracks the k most frequent item in the array
        for i in range(len(freq)-1,0,-1): #goes through frequencies in descending becuase the K most frequent items will be 
        # ranked from in descending order.
            for j in freq[i]: #goes through the list at rank k in case there are different numbers at the rank
                res.append(j) #adds each item to the results
                if len(res) == k: #stops when we have the k most frequent items
                    return res





 