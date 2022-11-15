class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i,j=0,0
        wordList = list(word)
        while j < len(word):
            if ch != wordList[j]:
                j +=1
            else:
                while i < j:
                    wordList[i],wordList[j] = wordList[j],wordList[i]
                    i +=1
                    j -=1
                break
        return "".join(wordList)
                
            
     