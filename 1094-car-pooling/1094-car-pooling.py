class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lengthOfTrip  = [0 for i in range(1001)]
        for passenger , fromi, toi in trips:
            lengthOfTrip[fromi] += passenger
            lengthOfTrip[toi] -= passenger
        num_passengers = 0
        for j in range(len(lengthOfTrip)):
            num_passengers += lengthOfTrip[j]
            if num_passengers > capacity:
                return False
        return True