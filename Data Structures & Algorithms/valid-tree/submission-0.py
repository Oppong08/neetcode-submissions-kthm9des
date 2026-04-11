class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #run dfs through to detect cycle

        graph = defaultdict(list)
        for node, edge in edges:
            graph[node].append(edge)

        seen = set()
        def dfs(node):
            if node in seen:
                return False
            if not node:
                return True

            seen.add(node)
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            return True
        
        return dfs(edges[0][1])