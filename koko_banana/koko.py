class Solution:
    def isGoodSpeed(self,speed,h,piles):
        hours = 0
        for index in range(len(piles)):
            hours += 1+ piles[index]//speed
            if piles[index]%speed ==0:
                hours-=1
        return hours<= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)+1
        while right - left > 1:
            mid = left + (right-left)//2
            if self.isGoodSpeed(mid,h,piles):
                right = mid
            else:
                left = mid
        return right





        