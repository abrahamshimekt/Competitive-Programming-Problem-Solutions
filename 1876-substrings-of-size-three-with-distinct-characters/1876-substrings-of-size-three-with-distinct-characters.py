class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        numberOfSubstring = 0
        while i + 3 <= len(s):
            first3 = s[i:i+3]
            countFirst3 = Counter(first3)
            isOne = True
            for letter in countFirst3:
                if countFirst3[letter] != 1:
                    isOne = False
            if isOne:
                numberOfSubstring +=1
            i +=1
        return numberOfSubstring
            
                    
                