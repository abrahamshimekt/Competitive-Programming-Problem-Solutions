class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        p = 0
        for i in range(2, n + 1):
            p = (k + p) % i
        return p + 1
        
