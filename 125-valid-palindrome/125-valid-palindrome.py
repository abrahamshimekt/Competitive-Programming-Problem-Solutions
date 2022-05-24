import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        alphabets = "abcdefghijklmnopqrstuvwxyz0123456789"
        for c in s:
            if c.lower() in alphabets:
                new_s +=c.lower()
        reveresed_s = ""
        for i in range(len(new_s)-1,-1,-1):
            reveresed_s += new_s[i]
        return new_s == reveresed_s