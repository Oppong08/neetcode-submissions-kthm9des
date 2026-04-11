class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #High level idea: build a graph of ordering rules between letters (for two words, the first character where they differ shows the ordering)
        #find a valid ordering of the graph using dfs topological sort
        #if there is a cycle, no valid ordering exists
        adj = {}
        for w in words:
            for c in w:
                adj[c] = []
        
        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen] :
                return ""
            for j in range(minLen): 
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])

        visited = {}
        res = []
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)


        # adj = {c: set() for w in words for c in w}

        # for i in range(len(words)-1):
        #     w1,w2 = words[i], words[i+1]
        #     minLen = min(len(w1), len(w2))
        #     #if two characters have the same prefix but first one is longer than second, return ""(invalid order)
        #     if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
        #         return ""
            
        #     for j in range(minLen):
        #         if w1[j] != w2[j]:
        #             adj[w1[j]].add(w2[j])
        #             break
        
        # visit = {}  #False = visited, True = visited & in current path
        # res = []

        # def dfs(c):
        #     if c in visit:
        #         return visit[c]

        #     visit[c] = True

        #     for nei in adj[c]:
        #         if dfs(nei):
        #             return True
            
        #     visit[c] = False
        #     res.append(c)
        
        # for c in adj:
        #     if dfs(c):
        #         return ""
        # res.reverse()
        # return "".join(res)