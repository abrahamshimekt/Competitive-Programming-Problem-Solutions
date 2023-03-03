class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x+1
        while high - low > 1:
            mid = low+(high-low)//2
            if mid <= x/mid:
                low = mid
            else:
                high = mid
        return low
        


         