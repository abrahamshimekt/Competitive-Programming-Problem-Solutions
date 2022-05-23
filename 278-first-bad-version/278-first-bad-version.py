# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower = 1
        upper = n
        bad = n
        while lower <= upper:
            mid =  (upper +lower)//2
            if isBadVersion(mid):
                bad = mid
                upper = mid-1
            else:
                lower = mid +1
        return bad
                
                
                
                
        