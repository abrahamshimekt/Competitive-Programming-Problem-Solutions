class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count +=1
        max_count = count
        i = 1
        while i + k <= len(s):
            if s[i-1] in vowels:
                count -= 1
            if s[i+k-1] in vowels:
                count +=1
            max_count = max(max_count,count)
            i +=1
        return max_count