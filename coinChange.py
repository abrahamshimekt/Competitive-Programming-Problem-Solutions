class Solution:
    def findMinCoin(self,coin):
        if coin == 0:
            return 0
        if coin < 0:
            return float("inf")
        if coin not in self.dp:
            minCoin = float("inf")
            for c in self.coins:
                minCoin = min(minCoin,1 + self.findMinCoin(coin-c))
            self.dp[coin] = minCoin
        return self.dp[coin]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = {}    
        self.coins = coins
        minCoin = self.findMinCoin(amount)
        return -1 if minCoin == float("inf") else minCoin
        
