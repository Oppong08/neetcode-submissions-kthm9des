class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #O(log(m+n))
        #for two sorted arrays, the combined array would contain at least half of each array in the left half and the right half
        
        A,B = nums1,nums2
        total = len(nums1) + len(nums2)
        half = total//2

        #run binary search on the smallest
        if len(B) < len(A):
            A,B = B, A

        l,r = 0, len(A) - 1
        while True:
            i = (l +r)//2   #index of mid element in A
            j = half - i - 2 #index of element in B

            #A represents the left sorted half
            Aleft = A[i] if i >= 0 else float("-infinity") #handles if A left is out of bounds
            Aright = A[i + 1] if(i+1) < len(A) else float("infinity") #handles if Aright is out of bounds
            #B represents the right sorted half
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                #odd 
                if total % 2:
                    return min(Aright, Bright)
                #even
                return (max(Aleft,Bleft) + min(Aright,Bright))/2

            #if wrong partition
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1















# # #my intuition: merge the two list, sort them and use binary search to find the median
        # # combined = sorted(nums1 + nums2)
        # # l, r = 0, len(combined)
        # # m = l+r//2
        # # return combined[m] if len(combined)%2 == 1 else (combined[m] + combined[m-1])/2

        # #O(log(m+n))
        # A, B = nums1, nums2
        # total = len(nums1) + len(nums2)
        # half = total//2

        # #run binary search on the shorter list for our left partition
        # if len(B) < len(A):
        #     A,B = B, A

        # l, r = 0, len(A) - 1
        # while True:
        #     i = (l+r)//2 #A
        #     j = half - i - 2 #B

        #     Aleft = A[i] if i >= 0 else float("-infinity")
        #     Aright = A[i + 1] if i + 1 < len(A) else float("infinity")
        #     Bleft = B[j] if j >= 0 else float("-infinity")
        #     Bright = B[j+1] if (j+1) < len(B) else float("infinity")

        #     # partition is correct
        #     if Aleft <= Bright and Bleft <= Aright:
        #         #odd
        #         if total % 2:
        #             return min(Aright,Bright)
        #         #even
        #         return (max(Aleft, Bleft) + min(Aright, Bright))/2
            
        #     elif Aleft > Bright:
        #         r = i - 1
            
        #     else:
        #         l += i + 1



