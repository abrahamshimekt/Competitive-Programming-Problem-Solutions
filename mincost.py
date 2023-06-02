class Solution:
    
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        steps = [0]*(n+2)
        for index in range(n-1,-1,-1):
            steps[index] = min(steps[index+1],steps[index+2]) + cost[index]
        return min(steps[0],steps[1])
       
        
