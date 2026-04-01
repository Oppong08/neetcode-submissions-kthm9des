class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:  #4#neet4#code4#love
            res +=  str(len(s)) + '#' + s 
        return res
        

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+1 + length])
            i = j + 1 + length
        return res



        
























        
        # #logic: use a number and a non-ascii character as a delimeter
        # res = ""
        # for s in strs:
        #     res += str(len(s)) + '#' + s 
        # return res
        # # res = ""
        # # for s in strs:
        # #     res += str(len(s)) + '#' + s
        # # return res


        # res = []
        # i = 0
        # while i < len(s):
        #     j = i 
        #     while s[j]!= '#':
        #         j += 1
        #     length = int(s[i:j])
        #     res.append(s[j+1:j+1+length])
        #     i = j + 1 + length
        # return res
        # # res, i = [],0
        # # while i < len(s):
        # #     j = i 
        # #     while s[j]!= '#':
        # #         j+=1
        # #     length = int(s[i:j])
        # #     res.append(s[j+1 : j+1+length])
        # #     i = j+1+length
        # # return res






























        
        
    





















        
        

        
