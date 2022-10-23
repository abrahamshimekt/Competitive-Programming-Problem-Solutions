class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "*" and i == 0:
                i += 1
            while stack and i < len(s) and s[i] == "*":
                stack.pop()
                i += 1
            if i < len(s) and s[i] != "*" :
                stack.append(s[i])
            i += 1
        return "".join(stack)