class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        p = Counter(p)
        anagram = Counter(s[:k])
        output = []
        i = 1
        while i + k <= len(s):
            if anagram == p:
                output.append(( i-1))
            anagram[s[i-1]] -= 1
            if s[k + i-1] not in anagram:
                anagram[s[k + i-1]] = 1
            else:
                anagram[s[k + i-1]] += 1
            i += 1
        if anagram == p:
            output.append(( i - 1))
        return output


                
            
        