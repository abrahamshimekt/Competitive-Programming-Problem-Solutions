class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while stones != []:
            if len(stones) == 1:
                return stones[0]
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            if x == y:
                continue
            elif x != y:
                stones.append(y-x)
        return 0
        
    
