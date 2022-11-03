class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i ,j = 0, len(tokens)-1
        score = 0
        while i <=j:
            if tokens[i] <= power:
                power -= tokens[i]
                score +=1
                i +=1
            elif tokens[j] > power and score >=1 and i!=j:
                power += tokens[j]
                score -=1
                j -=1
            else:
                i +=1
                j -=1
        
        return score
        