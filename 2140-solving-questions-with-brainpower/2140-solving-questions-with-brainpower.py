class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @lru_cache(None)
        def getPoints(i):
            if i >= n:
                return 0
            return max(getPoints(i + 1),questions[i][0]+ getPoints(i+questions[i][1] +1))
        return getPoints(0)
            