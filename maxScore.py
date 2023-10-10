class Solution:
    def gcd(self,x,y):
        if y == 0:
            return x
        return self.gcd(y,x%y)

    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def maximizeScore(state,step):
            if step >= n// 2 + 1:
                return 0
            if (state,step) in dp:
                return dp[(state,step)]
            maxScore = 0
            for x in range(n):
                if 1<< x & state:continue
                for y in range(x + 1,n):
                    if 1<<y & state: continue
                    maxScore = max(maxScore,step*self.gcd(nums[x],nums[y]) + maximizeScore(1<<x | 1<<y | state,step+1))
            dp[(state,step)] = maxScore
            return maxScore
        return maximizeScore(0,1)


        
        
