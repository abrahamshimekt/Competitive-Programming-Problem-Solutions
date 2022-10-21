class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        non_repeated = {s[0]:0}
        i,j= 0,1
        max_length = 0
        while i <len(s) and j <len(s):
            if s[j] not in non_repeated:
                non_repeated[s[j]] = 0
                j +=1
                if j==len(s):
                    max_length = max(max_length, len(non_repeated))
            else:
                max_length = max(max_length,len(non_repeated))
                non_repeated.pop(s[i])
                i +=1
        return max_length