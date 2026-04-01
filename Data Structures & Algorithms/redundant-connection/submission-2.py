class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Union Find Algorithm for cycle detection
        N = len(edges)
        par = [i for i in range(N+1)]
        rank = [1] * (N+1)

        def find(n): #function to find parent nodes
            if par[n] != n:
                return find(par[n])
            return par[n]

        def union(node1,node2):  #function to join two nodes if not joined alread
            p1,p2 = find(node1), find(node2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True


        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]


        # N = len(edges)
        # par = [i for i in range(N+1)]  #ith node -> parent(1 - n)
        # rank = [1] * (N+1)

        # def find(n):
        #     if n == par[n]:
        #         return par[n]
        #     # par[n] = 
        #     return find(par[n])

        
        # def union(n1, n2):
        #     p1, p2 = find(n1), find(n2)
        #     if p1 == p2:
        #         return False
            
        #     if rank[p1] > rank[p2]:
        #         par[p2] = p1
        #         rank[p1] += rank[p2]
        #     else:
        #         par[p1] = p2
        #         rank[p2] += rank[1]

        #     return True

        # for n1, n2 in edges:
        #     if not union(n1,n2):
        #         return [n1,n2]
        