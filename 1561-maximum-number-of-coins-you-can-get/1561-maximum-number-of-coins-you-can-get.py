class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        backT = n//3
        piles.sort()
        i = n-1
        my_score = piles[-2]
        while i >=0:
            if i == n-1:
                i -=2
                backT -=1
            elif backT > 0:
                my_score += piles[i-1]
                i -= 2
                backT -=1
            else:
                break
        return my_score
                
        