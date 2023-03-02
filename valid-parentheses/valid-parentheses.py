class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {"}":"{",")":"(","]":"["}
        for c in s:
            if stack and stack[-1] == par.get(c,None):
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
        