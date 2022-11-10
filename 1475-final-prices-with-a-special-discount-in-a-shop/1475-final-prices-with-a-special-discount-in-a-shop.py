class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answers = [0] * n
        stack = []
        i = 0
        while i < n:
            while stack and stack[-1][0] >= prices[i]:
                price, indx = stack.pop()
                answers[indx] = price - prices[i]
            stack.append([prices[i], i])
            i += 1
        for remain in stack:
            answers[remain[1]] = remain[0]
        return answers