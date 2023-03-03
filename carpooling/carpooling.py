class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_length = [0]*(1000+1)
        # this is a range query problem 
        for trip in trips:
            passenger,start,end = trip
            trip_length[start] += passenger
            trip_length[end] -= passenger

        for trip_i in range(1,1001):
            trip_length[trip_i] += trip_length[trip_i-1]

        for trip_j in range(1001):
            if trip_length[trip_j] > capacity:
                return False
            
        return True
        