class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #core idea: try to see if we can form an increasing group of the group size starting from the least number and the number of remaining numbers we have
        #count the occurence of each number using a hashmap, put the keys in a minH to always keep track of the least we have so far
        #for each smaller value, run an increasing loop upt to group size, if a number in the loop is not in our hashmap, return false(that group cannot be formed)
        #if we can form a valid group with the least number, reduce its count
        #if after reducing a numbers count, the count is 0, check if that number is not the least in the heap, before popping.
        #return True if we can form valid groups with each smaller number

        if len(hand) % groupSize:   
            return False
        
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n,0)
        
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1

                if count[i] == 0:  
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        return True

























        #greedy idea:
        #sort hands, if length of hands cannot be grouped into groupsize, return false
        #for i in range(0,len(hands), 4), extract the next list, see if the difference between any of the list is not one, return false