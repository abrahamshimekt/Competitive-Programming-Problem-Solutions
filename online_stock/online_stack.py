class StockSpanner:

    def __init__(self):
        self.stack =[]
    def next(self, price: int) -> int:
        days = 0
        
        while self.stack and self.stack[-1][0] <= price:

            days += self.stack[-1][1]
            self.stack.pop()
        days +=1

        self.stack.append([price,days])

        return days