class Solution:
    def numberOfSubstrings(self, s: str) -> int:  
        """ "ababbbc"
        i = 3
        j = 7
        count = 3
        seen = {a:0,b:3,c:1}
        
        """
        seen = {"a":0,"b":0,"c":0}
        i = j = 0
        count = 0
        n = len(s)
        while i + 3 <= n:
            if seen["a"] >=1 and seen["b"] >=1 and seen["c"] >=1:
                seen[s[i]] -=1
                i +=1
                count += n-j+1
            else:
                if j <= n-1:
                    seen[s[j]] +=1
                    j +=1
                else:
                    i +=1
        return count
            