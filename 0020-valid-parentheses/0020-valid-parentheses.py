class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {")":"(","}":"{","]":"["}
        stack = []
        for c in s:
            if stack and stack[-1] == parenthesis.get(c):
                stack.pop()
            else:
                stack.append(c)
        return stack ==[]
        
            
            
            