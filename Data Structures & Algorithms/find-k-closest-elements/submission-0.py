class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #sliding window
        l, r  = 0, len(arr) - k
        while l < r:
            #left most value of the window
            m = (l + r)//2
            #if the value to the right is closer than the left
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l+k]



