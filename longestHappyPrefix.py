class Solution:
    def longestPrefix(self, s: str) -> str:

        n = len(s)
        lps = [0]*n
        length = 0
        i = 1
        while i < n:
            if s[length] == s[i]:
                length +=1
                lps[i] = length
                i +=1
            elif length == 0:
                lps[i] = 0
                i +=1
            else:
                length = lps[length-1]

        start = n - lps[n-1] 
        return s[start:]

