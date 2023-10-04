class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = {}
        def findMinCost(index,countA,countB):
            if countA > n//2:
                return float('inf')
            if countB > n//2:
                return float('inf')
            if index >= n:
                return 0
            if (index,countA,countB) in dp:
                return dp[(index,countA,countB)]
            goToA = costs[index][0] + findMinCost(index+1,countA+1,countB)
            goToB = costs[index][1] + findMinCost(index+1,countA,countB+1)
            dp[(index,countA,countB)] = min(goToA,goToB)
            return dp[(index,countA,countB)] 

        return findMinCost(0,0,0)
        
