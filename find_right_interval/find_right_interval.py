class Solution:
    def findIntervalIndex(self,starts,end):
        left = -1
        right = len(starts)
        while right - left > 1:

            mid = left + (right - left)//2
            if starts[mid][0]>=end:
                
                right = mid
            else:
                left = mid

        return right

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        starts = []

        for index in range(len(intervals)):
            starts.append([intervals[index][0],index])

        starts.sort()

        right_interval = []

        for indxx in range(len(intervals)):

            interval = intervals[indxx]
            end = interval[1]
            start_index = self.findIntervalIndex(starts,end)

            if start_index == len(starts):

                right_interval.append(-1)

            else:
                start = starts[start_index][1]
                right_interval.append(start)

        return right_interval

            


