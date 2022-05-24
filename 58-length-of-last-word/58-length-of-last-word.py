class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split()
        return len(s_list[-1])