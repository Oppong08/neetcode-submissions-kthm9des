from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #first build adjacency list with prerequisites
        prereq = defaultdict(list)
        for crs,pre in prerequisites:
            prereq[crs].append(pre)
        
        #a coures has 3 possible states:
        #visitied -> crse has been added to output
        #visiting -> cres not added to output, but added to cycle
        #unvisited -> cres not added to output or cycle



        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

        #loop through each course, run dfs to find if pre-requisite can be completed
        

        #add completed course to list

