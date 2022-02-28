from ast import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            while stack !=[] and temp > stack[-1][1]:
                stackInd,stackT = stack.pop()
                output[stackInd] = (i - stackInd)
            stack.append([i,temp])
        return output