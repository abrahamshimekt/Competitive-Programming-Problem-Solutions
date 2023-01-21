class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        my_coins = 0
        piles.sort()
        left = 0
        right = len(piles)-3
        while left <= right :
            my_coins += piles[right +1]
            left +=1
            right -= 2
        return my_coins