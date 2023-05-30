from heapq import *
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        for index in range(n):
            piles[index] = -piles[index]
        heapify(piles)
        for operation in range(k):
            currNum = -heappop(piles)
            heappush(piles,-(currNum-currNum//2))
        return -sum(piles)

