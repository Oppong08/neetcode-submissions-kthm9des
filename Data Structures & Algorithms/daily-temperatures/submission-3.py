class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #bruteforce: for every item, have a counter that counts the next time we get a warmer item and add to res
        # res = []
        
        # for i in range(len(temperatures)):
        #     count = 1
        #     j = i + 1
        #     while j < len(temperatures):
        #         if temperatures[j] > temperatures[i]:
        #             break
        #         j +=1
        #         count+=1
        #     count = 0 if j == len(temperatures) else count
        #     res.append(count)
        # return res
            
    
    #go through the list, add value to stack, 
    #keep addin to the stack as long as we've not found a value greater than the to p of the stack
    #if we find a greater temperature, keep comparing it to the top of the stack
    #at each coparison, add the difference between the index to res at index
    
    #pop and add the new one to stakck while recording the counts 

        stack = [] #contains pair [temperature, index]
        res = [0]* len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]: 
                stackIndex, stackT = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([i,t])
        return res

        


