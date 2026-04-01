class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #logic: use a map to connect courses to their prerequisites in a graph
        #run dfs through each prerequisite, to see if it can be completed and mark them as such
        #return True if all courses can be completed else false


        #map each course to their pre-requisites using a hasmap
        #courseMap = {i:[] for i in range(numCourses)}
        courseMap = defaultdict(list)
        for crs, pre in prerequisites:
            courseMap[crs].append(pre)

        #hashset to store visited nodes in the dfs
        visited = set()
        
        def dfs(crs):
            #base cases1: if course in visited already, return False(cycle detected)
            if crs in visited:
                return False
            
            #base case 2: if course has no prerequisit, return True (it can be completed)
            if courseMap[crs] == []:
                return True
            
            #add cur course to visited set
            visited.add(crs)
            #recursive case: run dfs on all prerequisits to see if they can completed
            for pre in courseMap[crs]:
                if not dfs(pre):
                    return False
            #remove crs from set and mark it as completed
            visited.remove(crs)
            courseMap[crs] = []
            return True
        
        #call dfs on each course in numCourses
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



         
        
        
        
        
        
        
        


    
            
                

        