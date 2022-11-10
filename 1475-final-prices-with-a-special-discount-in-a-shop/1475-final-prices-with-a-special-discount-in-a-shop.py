class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answers = []
        for i in range(n-1):
            found = False
            for j in range(i +1,n):
                if prices[i] >= prices[j]:
                    found = True
                    answers.append(prices[i]-prices[j])
                    break
            if not found:
                answers.append(prices[i])
        answers.append(prices[-1])
        return answers