from collections import Counter
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Each CPU cycle allows the completion of a single task
        #The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

        #logic: pop most recently occuring task out of heap, perform one and add the remainder to 
        # the que until time 1 + n is reached where it can be available again
        #add it back to the heap and reapeat until que or heap is empty. that's the most appropriate sequence for us to achieve the minimum cycle counts

        count = Counter(tasks) #counts each character into a hasmap
        
        #creates a maxheap based on occurence of each task
        maxheap = [-cnt for cnt in count.values()] 
        heapq.heapify(maxheap)

        q = deque() # [ pairs of [-cnt, idletime] que for storing remaining tasks and time for the next availability 
        time = 0    #checking the next time a task can be available to complete after the 1 cycle 
        
        while q or maxheap:
           

            if maxheap: #if there are items in the maxheap, popp it and process it, reducing its remaining counts by 1.
                        #in this case adding one to its negative cnt value
                cnt = 1 + heapq.heappop(maxheap)
                

                if cnt: #if count is not zero, add it to the que and its remaining time by adding to our idle time n
                    q.append([cnt,time + n])
            
            #when the idle time is reached for the task, we pop it out the que and adds it back to the heap for processing
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
            
            time +=1

            

        return time








