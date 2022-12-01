class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = ""
        b = ""
        n = len(s)
        for i in range(n):
            if i < n//2:
                a +=s[i]
            else:
                b +=s[i]
        vowels_in_a = 0
        vowels_in_b = 0
        for c in a:
            if c in "aeiouAEIOU":
                vowels_in_a +=1
        for c in b:
            if c in "aeiouAEIOU":
                vowels_in_b +=1
        return vowels_in_a == vowels_in_b
        