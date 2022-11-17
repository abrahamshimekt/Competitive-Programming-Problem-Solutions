class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        word = list(s)
        i,j = 0,len(s)-1
        while i < j:
            if word[i] not in vowels:
                i +=1
            elif word[j] not in vowels:
                j -=1
            else:
                word[i],word[j] = word[j],word[i]
                i +=1
                j -=1
        return ''.join(word)
                
                
        