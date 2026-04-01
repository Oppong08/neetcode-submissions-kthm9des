class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #"zxyzxyz"
        seen = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[i])
            res = max(res, i - l + 1)

        return res


        # charset = set()
        # res = 0
        # i = 0
        # for r in range(len(s)):
        #     while s[r] in charset:
        #         charset.remove(s[i])
        #         i+=1
        #     charset.add(s[r])
        #     res = max(res,r - i + 1)
        # return res
       














       



        # if not s:
        #     return 0
        # longest = 1
        # count = 1
        # l,r = 0, 1
        # map = {}
        # while r < len(s):
        #     map[s[r]] = 1 + map.get(s[r], 0)
        #     count += 1
        #     longest = max(count, longest)
        #     if s[r] in map:
        #         map = {}
        #         count = 0 
        #         l = r
        #         r+= 1
        # return longest

            

        