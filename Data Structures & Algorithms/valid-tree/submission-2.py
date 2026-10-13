class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #logic: a tree is a fully connected graph with no cycles
        #run dfs through to detect cycle, return False if there is 
        #to handle the fact that each node is undirected ( connected connected to the previous node and its listsed edge):

        #connect each elements to each other
        graph = defaultdict(list) 

        for node, edge in edges:
            graph[node].append(edge)
            graph[edge].append(node)
        
        seen = set() 

        def dfs(node, prev):
            if node in seen:
                return False
            
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True


        return dfs(0,-1) and len(seen) == n

























        # #use a pointer to mark each previous node
        # if not n:
        #     return false

        # graph = collections.defaultdict(list)
        # for node, edge in edges:
        #     graph[node].append(edge)
        #     graph[edge].append(node)

        # seen = set()
        # def dfs(node,prev):
        #     if node in seen:
        #         return False
            
        #     seen.add(node)
        #     for neigh in graph[node]:
        #         if neigh == prev:
        #             continue
        #         if not dfs(neigh,node):
        #             return False
        #     return True
        
        # #return true if dfs(0) and we visited all nodes(all nodes are connected)
        # return dfs(0,-1) and len(seen) == n