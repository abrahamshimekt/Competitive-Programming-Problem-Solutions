class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        r = len(cost)-1
        itemNumber =0
        minCost = 0
        while r >-1:
            if itemNumber <2:
                minCost += cost[r]
                itemNumber +=1
                r -=1
            else:
                itemNumber =0
                r -=1
        return minCost
                
            
                
            
        