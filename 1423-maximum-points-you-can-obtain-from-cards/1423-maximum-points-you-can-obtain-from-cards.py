class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        score = 0
        n = len(cardPoints)
        for i in range(k):
            score += cardPoints[i]
        curr_score = score
        for j in range(k - 1, -1, -1):
            curr_score -= cardPoints[j]
            curr_score += cardPoints[n - k + j]
            score = max(score,curr_score)
        return score