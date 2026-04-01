class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #bruteforce
        res = set()
        candidates.sort()
        def dfs(i, curpath, total):
            if total == target:
                res.add(tuple(curpath))
                return
            if i == len(candidates) or total > target:
                return
            curpath.append(candidates[i])
            dfs(i+ 1, curpath, total + candidates[i])
            curpath.pop()
            dfs(i + 1, curpath, total)

        dfs(0,[],0)
        return [list(combination) for combination in res]