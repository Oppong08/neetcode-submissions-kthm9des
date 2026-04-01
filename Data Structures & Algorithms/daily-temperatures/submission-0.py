class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #bruteforce: for every item, have a counter that counts the next time we get a warmer item and add to res
        res = []
        
        for i in range(len(temperatures)):
            count = 1
            j = i + 1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    break
                j +=1
                count+=1
            count = 0 if j == len(temperatures) else count
            res.append(count)
        return res
            
        
        return res

