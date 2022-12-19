class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        for word in strs:
            n = len(word) 
            if n < min_length:
                min_length = n
        m =  len(strs)
        if m==min_length==1:
            return strs[0]
        ans = ""
        c = ""
        common = True
        for i in range(min_length):
            for j in range(m-1):
                if strs[j][i] != strs[j+1][i]:
                    common = False
                else:
                    c = strs[j][i]
            if common:
                ans += c
        return ans