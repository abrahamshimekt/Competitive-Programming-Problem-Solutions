class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        i=j=1
        n = len(s)
        opening_count = 1
        closing_count = 0
        result = ""
        while j<n: 
            if  opening_count != closing_count:
                if s[j] == "(":
                    opening_count +=1
                else:
                    closing_count +=1
                j +=1
                if j ==n and  opening_count == closing_count :
                    result += s[i:j-1]
            else:
                result += s[i:j-1]
                j += 1
                i = j
                opening_count = 1
                closing_count = 0
        return result
                
                
            
                    
                    