class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum  =[gain[0]]
        heighest_altitude =max(0,prefix_sum[0])
        for i in range(1,len(gain)):
            prefix_sum.append(prefix_sum[i-1] + gain[i])
            heighest_altitude = max(heighest_altitude,prefix_sum[i])
        return heighest_altitude
            