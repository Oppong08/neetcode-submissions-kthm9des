class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #logic not doing the actual replacement,just checking for the maximum length within which we can make k
        #replacements
        #how do we know: we'd look for the least occuring letter and its frequency if its within k else check a different window
        
        count = {} #keep count of characters within our current window
        l = 0       #begining of window
        res = 0    #initial count of longest window
        maxf = 0      #keeps track of maximum frequency of most occuring character withing a window
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf, count[s[r]])
            #while/if the less frequent character in current window is more than K(ie, we'd have to make more than k replacements), we check a new window
            if (r-l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res,r-l + 1)
        return res
    








        
        
        # count = {}
        # l = 0
        # res = 0
        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)

        #     while (r - l + 1) - max(count.values()) > k: #Check for valid window
        #         count[s[l]] -= 1
        #         l += 1
        #     res = max(res, r - l + 1 )
        # return res




