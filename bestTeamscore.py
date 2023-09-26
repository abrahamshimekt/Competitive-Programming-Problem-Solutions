class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scoreHashMap = {}
        n = len(ages)
        agesScores = []
        for i in range(n):
            agesScores.append((ages[i],scores[i]))
        agesScores.sort()
        dp = [0]*n
        def findBestScore(i):
            if i >= n:
                return 0
            if dp[i] != 0:
                return dp[i]
            maxScore = agesScores[i][1]
            for j in range(i+1,n):
                if agesScores[j][1] >= agesScores[i][1]:
                    maxScore = max(maxScore,agesScores[i][1] + findBestScore(j))
            dp[i] = maxScore
            return dp[i]
        maxScore = 0
        for index in range(n):
            maxScore = max(maxScore,findBestScore(index))
        return maxScore


            


        
