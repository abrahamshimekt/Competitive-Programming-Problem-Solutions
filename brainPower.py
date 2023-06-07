class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp ={}
        def earnMaxPoints(index):
            if index >=n:
                return 0
            if index not in dp:
                skip = questions[index][1]
                dp[index] = max(earnMaxPoints(index + skip + 1) + questions[index][0],earnMaxPoints(index+1))
            return dp[index]
        return earnMaxPoints(0)
        
