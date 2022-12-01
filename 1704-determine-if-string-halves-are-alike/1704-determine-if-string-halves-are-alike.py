class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a  = s[:n//2]
        b = s[n//2:]
        vowels_in_a = 0
        vowels_in_b = 0
        for c in a:
            if c in "aeiouAEIOU":
                vowels_in_a +=1
        for ch in b:
            if ch in "aeiouAEIOU":
                vowels_in_b +=1  
        return vowels_in_a == vowels_in_b
        
        