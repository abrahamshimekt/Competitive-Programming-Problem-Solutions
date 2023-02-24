class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {}
        stack = []
        visited = set()
        for index in range(len(s)):
            last_occur[s[index]] = index 
        for index_ in range(len(s)):
            if s[index_] not in visited:
                while stack and stack[-1] >= s[index_] and last_occur[stack[-1]] > index_:
                    visited.remove(stack[-1])
                    stack.pop()
                stack.append(s[index_])
                visited.add(s[index_])
        return ''.join(stack)
            
