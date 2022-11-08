class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if stack and abs(ord(stack[-1])-ord(s[i])) == 32:
                stack.pop()
                i +=1
            else:
                stack.append(s[i])
                i +=1
        return "".join(stack)