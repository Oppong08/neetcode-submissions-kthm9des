class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #my intuition: merge the two list, sort them and use binary search to find the median
        combined = sorted(nums1 + nums2)

        l, r = 0, len(combined)
        m = l+r//2
        return combined[m] if len(combined)%2 == 1 else (combined[m] + combined[m-1])/2

        