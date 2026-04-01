class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curpath, total):
            if total == target:
                res.append(curpath.copy())
                return

            if total > target or i >= len(candidates):
                return 
            
            #include candidates[i]
            curpath.append(candidates[i])
            dfs(i+1, curpath, total + candidates[i])
            curpath.pop()

            #skip candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 
            dfs(i+1, curpath, total)
        
        dfs(0,[],0)

        return res



















        #bruteforce
        # res = set()
        # candidates.sort()
        # def dfs(i, curpath, total):
        #     if total == target:
        #         res.add(tuple(curpath))
        #         return
        #     if i == len(candidates) or total > target:
        #         return
        #     curpath.append(candidates[i])
        #     dfs(i+ 1, curpath, total + candidates[i])
        #     curpath.pop()
        #     dfs(i + 1, curpath, total)

        # dfs(0,[],0)
        # return [list(combination) for combination in res]