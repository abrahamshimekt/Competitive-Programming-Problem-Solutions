class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_dictionary = Counter(s1)
        i, j = 0,k
        while i + k <= len(s2):
            if Counter(s2[i:j]) == s1_dictionary:
                return True
            i +=1
            j +=1
        return False