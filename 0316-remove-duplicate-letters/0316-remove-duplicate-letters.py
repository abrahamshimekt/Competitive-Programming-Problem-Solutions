from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {}
        seen = {}
        stack = []
        n = len(s)
        for i in range(n):
            last_occ[s[i]] = i
        for j in range(n):
            if s[j] not in seen:
                while stack and stack[-1] > s[j] and last_occ[stack[-1]] > j:
                    seen.pop(stack.pop())
                stack.append(s[j])
                seen[s[j]] = 1
        return "".join(stack)
       
                
                    
            
                
        
        
       
            
            
            
                
            
            
        