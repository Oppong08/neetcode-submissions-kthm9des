class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
       
        #core logic: if the sum of all gas is less than the sum of all cost, it is impossible to complete a loop to all stations
        #At each index(gas station), compute total remaining gas by subtracting cost[i] and adding gas[i]
        #if at any point, the total falls less than 0, reset the toal and start from the next index
        #return the index at the end of the loop 
        
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1
        
        return res
            
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if sum(gas) < sum(cost):
        #     return -1

        # total = 0
        # res = 0
        # for i in range(len(gas)):
        #     total += (gas[i] - cost[i])

        #     if total < 0:
        #         total = 0
        #         res = i + 1

        # return res


         # if sum(gas) < sum(cost):
        #     return - 1
        
        # total = 0
        # res = 0 
        
        # for i in range(len(gas)):
        #     total += (gas[i] - cost[i])

        #     if total < 0:
        #         total = 0
        #         res = i + 1
        
        # return res

