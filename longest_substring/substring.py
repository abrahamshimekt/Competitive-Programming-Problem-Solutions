class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left = 0
        max_l = 0
        for right in range(len(s)):
            while s[right] in unique:
               unique.remove(s[left])
               left +=1
            unique.add(s[right])
            max_l = max(max_l,right-left+1)
        return max_l

