class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
       #using union find to connect the nodes
        
        #initiate parent and rank lists
        par = [i for i in range(n)] 
        rank = [1] * n

        #finds the parent node of a node
        def find(n1):
            res = n1  
            while res != par[res]: #while the results is not a parent of itself 
                par[res] = par[par[res]] #path compression , by setting current parent's parent to its granparent
                res = par[res]     #increment result to the parent of the current res
            
            return res


        #connects/merges two nodes together after finding their parents
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            #if already merged to have the same parent
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]: #if rank of p2 is greater than that of p1:
                par[p1] = p2      #set p2 as parent of p1
                rank[p2] += rank[p1] #increase the rank of p2

            else:                  #else do the opposite, return as one union done
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n 
        #move through each edge and return if / not a succesful union and update count
        for n1,n2 in edges:
            res -= union(n1,n2)
        return res



