class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None]*26

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        offSet = 97
        for char in word:
            index = ord(char)-offSet
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEnd = True

        
    def search(self, word: str) -> bool:
        return self.searchWord(0,word,self.root)
      
    def searchWord(self,i,word,node):
        if i == len(word):
            return node.isEnd
        if word[i] == ".":
            for j in range(26):
                if node.children[j] and self.searchWord(i + 1,word,node.children[j]):
                    return True
            return False
        index = ord(word[i])-97
        if not node.children[index]:
            return False
        return self.searchWord(i+1,word,node.children[index])
        



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
