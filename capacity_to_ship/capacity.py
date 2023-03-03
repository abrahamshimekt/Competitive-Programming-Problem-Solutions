class Solution:
    def isGoodCapacity(self,capacity,weights,days):
        curr_days = 1
        curr_capacity = 0
        for index in range(len(weights)):
            curr_capacity += weights[index]
            if curr_capacity > capacity:
                curr_capacity =  weights[index]
                curr_days +=1
        return curr_days<=days
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)-1
        total = sum(weights)
        right = total + 1
        while right - left >1:
            mid = left + (right-left)//2
            if self.isGoodCapacity(mid,weights,days):
                right = mid
            else:
                left = mid
        
        return right