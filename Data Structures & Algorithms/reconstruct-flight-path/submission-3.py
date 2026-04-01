class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #path will always start with jfk
        #create a graph connecting airports in sorted order
        graph = defaultdict(list)
        tickets.sort()
        for src, dest in tickets:
            graph[src].append(dest)

        
        res = ["JFK"]
        visit = set()
        #use dfs to travers the graph from the destination point, backtrack if not a valid path
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True

            if src not in graph:
                return False

            temp = list(graph[src])    
            for i,v in enumerate(temp):
                graph[src].pop(i)
                res.append(v)
                
                if dfs(v):
                    return True
                
                graph[src].insert(i,v)
                res.pop()
            return False
        dfs("JFK")
        return res

        #create sorted adjacency list 
        # adj = {src: [] for src, dst in tickets}
        # tickets.sort()
        # for src, dst in tickets:
        #     adj[src].append(dst)
        # res = ["JFK"]
        # def dfs(src):
        #     #base case
        #     if len(res) == len(tickets) + 1:
        #         return True
            
        #     if src not in adj:
        #         return False

        #     temp = list(adj[src])
        #     for i, v in enumerate(temp):
        #         adj[src].pop(i)
        #         res.append(v)

        #         if dfs(v):
        #             return True
                
        #         adj[src].insert(i,v)
        #         res.pop()
        #     return False
        # dfs("JFK")
        # return res

                

