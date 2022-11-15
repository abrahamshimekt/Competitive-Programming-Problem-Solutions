class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stonesCount = {}
        n = len(stones)
        for stone in stones:
            if stone not in stonesCount:
                stonesCount[stone] = 1
            else:
                stonesCount[stone] +=1
        jewelsInStone = 0
        for jewel in jewels:
            if jewel in stonesCount:
                jewelsInStone += stonesCount[jewel]
        return jewelsInStone
            