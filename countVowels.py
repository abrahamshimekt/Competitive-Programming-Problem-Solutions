class Solution:
    def countVowels(self, word: str) -> int:
        numOfSubstrings = 0
        n = len(word)
        
        for index in range(n):
            if word[index] in "aeiou":
                starting = index + 1
                ending = n - index
                numOfSubstrings += starting * ending
        return numOfSubstrings

        
