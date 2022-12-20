def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        i=j=0
        n = len(word1)
        m = len(word2)
        while i < n or j < m:
            if i < n:
                 merged += word1[i]
            if j < m:
                 merged += word2[j]
            i +=1
            j +=1
        return merged