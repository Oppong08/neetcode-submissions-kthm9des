class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for k in range(n+1):
            # k = bin(i)[2:]
            res = 0
            while k:
                k &= (k-1)
                res+= 1
            arr.append(res)
        return arr


