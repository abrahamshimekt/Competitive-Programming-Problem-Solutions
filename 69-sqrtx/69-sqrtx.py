class Solution:
    def mySqrt(self, x: int) -> int:
        start ,end = 1,x
        ans = 0
        while start <= end:
            mid = start + (end-start)//2
            if (mid<= x/mid):
                start = mid +1
                ans = mid
            else:
                end = mid-1
        return ans