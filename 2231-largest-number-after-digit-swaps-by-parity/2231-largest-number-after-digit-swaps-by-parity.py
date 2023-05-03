import heapq
class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        evenDigits = [-d for d in digits if not d%2]
        oddDigits = [-d for d in digits if d% 2]
        
        heapq.heapify(evenDigits)
        heapq.heapify(oddDigits)
        LargestNum = 0
        for digit in digits:
            if digit % 2:
                currMaxNum = heapq.heappop(oddDigits)
                heapq.heapify(oddDigits)
                LargestNum = LargestNum * 10 + -currMaxNum
            else:
                currMaxNum = heapq.heappop(evenDigits)
                heapq.heapify(evenDigits)
                LargestNum = LargestNum * 10 + -currMaxNum
        
        return LargestNum
                
                

        
        