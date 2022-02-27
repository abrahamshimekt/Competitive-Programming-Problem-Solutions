class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack =[]
        par = {}
        for i,k in enumerate(s):
            if k =='(':
                stack.append(i)
            elif k == ')':
                j = stack.pop()
                par[i] = j
                par[j] = i
        outPut = ""
        d = 1
        i = 0
        while i<n:
            if s[i] in  '()':
                i = par[i]
                d = -d
            else:
                outPut += s[i]
            i +=d
        return outPut