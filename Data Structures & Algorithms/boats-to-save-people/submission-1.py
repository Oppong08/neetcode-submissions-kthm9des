class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #greedy:
        #logic: sort the array from least to highest weigt, start pairing the heaviest with the lighest if they're within limits, 
        #
        people.sort()
        res = 0
        l, r = 0, len(people)-1
        while l <= r:
            remain = limit - people[r]
            r -=1 
            res += 1

            #if there's more room at add the least with the current heaviest, add it to the pair
            if l <= r and remain >= people[l]: 
                l += 1
        
        return res
