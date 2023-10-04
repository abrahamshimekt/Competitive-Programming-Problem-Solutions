class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        n = len(satisfaction)
        total = 0
        for i in range(n):
            total += (i+1)*satisfaction[i]
            
        prefixSum = [0]*n
        prefixSum[-1] = satisfaction[-1]
        
        for j in range(n-2,-1,-1):
            
            prefixSum[j] = prefixSum[j +1] + satisfaction[j]
        maxLikeTime = total
        
        for k in range(n-1):
            total -= (satisfaction[k]+ prefixSum[k+1])
            maxLikeTime = max(maxLikeTime,total)
            
        return maxLikeTime if maxLikeTime>= 0 else 0
            
        
