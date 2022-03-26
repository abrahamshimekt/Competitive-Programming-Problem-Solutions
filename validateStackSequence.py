class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack =[]
        numOfPopped =0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                numOfPopped +=1
                stack.pop()
        return numOfPopped == len(popped)