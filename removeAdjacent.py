class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        n = len(s)
        for index in range(n-1,-1,-1):
            enter = False
            if stack and stack[-1][0] == s[index] and stack[-1][1] + 1 == k:
                enter = True
                stack.pop()
            if stack and stack[-1][0] == s[index]:
                char,count = stack.pop()
                stack.append((char,count+1))
            elif not enter:
                stack.append((s[index],1))
        m = len(stack)
        ans = []
        for j in range(m-1,-1,-1):
            ans.append(stack[j][0]*stack[j][1])

        return "".join(ans)
        
            
        
