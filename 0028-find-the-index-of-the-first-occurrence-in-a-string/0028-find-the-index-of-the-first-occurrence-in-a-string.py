class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        i = 0
        while i + k <= len(haystack):
            if haystack[i:k+i] == needle:
                return i
            i +=1
        return -1