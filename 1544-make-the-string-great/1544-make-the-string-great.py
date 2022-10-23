class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            while stack and (abs(ord(stack[-1]) - ord(s[i])) == 32 or abs(ord(s[i]) - ord(stack[-1])) == 32):
                stack.pop()
                i += 1
                if i == len(s):
                    break
            else:
                if i < len(s):
                    stack.append(s[i])
                i += 1
        return "".join(stack)