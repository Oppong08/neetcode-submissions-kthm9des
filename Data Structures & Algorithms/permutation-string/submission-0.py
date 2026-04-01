class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #my logic : comparing sequence in both strings
        #bruteforce:
        s1 = sorted(s1)
        for i in range(len(s2)):
            for j in range(i,len(s2)):
                substr= s2[i:j+1]
                substr = sorted(substr)
                if substr == s1:
                    return True
        return False


        #Hash Table: logic: similar to anagrams, count of each item could be used to check for possible permutations
        count1 = {}
        for c in s1: #counts 
            count1[c] = 1 + count1.get(c,0)
        
        need = len(count1) # number of distinct character counts needed

        for i in range(len(s2)):
            #count2 tracks the count of each character in s2., cur checks if 
            #we've reached the same number of distinct characters as in s1
            count2, cur = {}, 0 
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j],0)

                #if counts of first is less than that of second for a particular character
                #implies not possible to get a permutation
                if count1.get(s2[j]) < count2.get(s2[j]):
                    break

                #if equal counts of a particular character appears
                #increase current lenght until last condition
                if count1.get(s2[j],0) == count2[s2[j]]:
                    cur += 1
                
                
                #if we have our desired counts of s1 characters in s2
                if cur == need:
                    return True
        
        return False

                
                

            


        
