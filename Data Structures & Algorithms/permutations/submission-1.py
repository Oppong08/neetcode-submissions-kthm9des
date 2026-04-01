class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        res = []
        perms = self.permute(nums[1:])
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res






















        #base case  
        # if len(nums) == 0:
        #     return [[]]
        
        # #recursively find the permutations of the list except the first one and store it in perms
        # perms = self.permute(nums[1:])
        # res = []
        
        # #for each permutation copy, insert the first item into each position i and add to result
        # #return the res to up the recursive tree
        # for p in perms: 
        #     for i in range(len(p)+1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)
        # return res

