class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for s in strs:
            res[str(sorted(s))].append(s)
        
        return list(res.values())
            




        #bruteforce: Go through compare lengths, before characters, group later
        # res = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c)-ord('a')]+=1
        #     res[tuple(count)].append(s)
        # return list(res.values())
        