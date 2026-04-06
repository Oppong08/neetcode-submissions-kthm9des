class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for w in strs:
                if i == len(w) or w[i] != strs[0][i]:
                    return w[:i]
        
        return strs[0]     

        # res = ""
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or s[i] != strs[0][i] :
        #             return res
        #     res += strs[0][i]
        # return res