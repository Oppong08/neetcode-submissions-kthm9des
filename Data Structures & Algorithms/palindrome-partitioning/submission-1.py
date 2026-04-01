class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #bigger logic: try generating all possible substrings, add the palindromic substrings to the res

        res = []
        cur = []
        def dfs(i):
            #base case:
            if i >= len(s):
                res.append(cur.copy())
                return

            #recursive
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    cur.append(s[i:j+1])
                    dfs(j+1)
                    cur.pop()
        dfs(0)
        return res
    def isPali(self, s,l,r):
       
        while l < r:
            if s[l] != s[r]:
                return False
            l +=1
            r -= 1
        return True

    #     res = []  #stores list of all valid palindromic partitions
    #     part = [] #stores current palindromic substrings in a partition

    #     def dfs(i):
    #         #base case: if we reach the last element add part to res
    #         if i >= len(s):
    #             res.append(part.copy())
    #             return
            
    #         #generate only palindromic substrings from current index to the end
    #         for j in range(i, len(s)):
    #             if self.isPali(s, i, j):
    #                 part.append(s[i:j+1]) 
    #                 dfs(j + 1)
    #                 part.pop()
    #     dfs(0)
    #     return res

    # #helper to determine if a substring from i - j is a palindrom
    # def isPali(self,s, l, r):
    #     while l<r:
    #         if s[l]!= s[r]:
    #             return False
    #         l+=1
    #         r-=1
    #     return True