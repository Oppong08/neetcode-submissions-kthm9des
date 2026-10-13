   #using union find to connect the nodes
class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n
     
    def find(self,node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur
        # if parent[x] != x:
        #     parent[x] = find[parent[x]]
        # return parent[x]
        
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv :
            return False
        if self.rank[pv] > self.rank[pu]:
            pu,pv = pv, pu

        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        dsu = DSU(n)
        res = n
        for u,v in edges:
            if dsu.union(u,v):
                res -= 1
        return res
        # if rank[par_x] > rank[par_y]:
        #     par[x] = par[x]
        # elif rank[par_x] < rank[par_y]:
        #     par[x] = par[y]
        # else:
        #     par[y] = x
        #     rank[x] += 1
            































    #     #initiate parent and rank lists
    #     par = [i for i in range(n)] 
    #     rank = [1] * n

    #     #finds the parent node of a node
    #     def find(n1):
    #         res = n1  
    #         while res != par[res]: #while the results is not a parent of itself 
    #             par[res] = par[par[res]] #path compression , by setting current parent's parent to its granparent
    #             res = par[res]     #increment result to the parent of the current res
            
    #         return res


    #     #connects/merges two nodes together after finding their parents
    #     def union(n1, n2):
    #         p1, p2 = find(n1), find(n2)

    #         #if already merged to have the same parent
    #         if p1 == p2:
    #             return 0
            
    #         if rank[p2] > rank[p1]: #if rank of p2 is greater than that of p1:
    #             par[p1] = p2      #set p2 as parent of p1
    #             rank[p2] += rank[p1] #increase the rank of p2

    #         else:                  #else do the opposite, return as one union done
    #             par[p2] = p1
    #             rank[p1] += rank[p2]
    #         return 1

    #     res = n 
    #     #move through each edge and return if / not a succesful union and update count
    #     for n1,n2 in edges:
    #         res -= union(n1,n2)
    #     return res



