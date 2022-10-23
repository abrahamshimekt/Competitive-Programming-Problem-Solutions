class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days_to_wait = [0]*len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT,indx = stack.pop()
                days_to_wait[indx] = i - indx
            stack.append([t,i])
        return days_to_wait