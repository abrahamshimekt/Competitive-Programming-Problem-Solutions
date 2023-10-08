class TrieNode:
    
    def __init__(self):
        self.childrens = {}
        self.isEnd = False
        self.count = 0
        
    
class Solution:
     
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.childrens:
                node.childrens[char] = TrieNode()
            node = node.childrens[char]
        node.isEnd = True
        node.count += 1  
    
    def findIndex(self, word, start, cur_char):
        for i in range(start, len(word)):
            if word[i] == cur_char:
                return i
        return -1
    
    def dfs(self, node, word, start):
        for char, child in node.childrens.items():
            index = self.findIndex(word, start, char)
            if index != -1:
                if child.isEnd:
                    self.count += child.count
                self.dfs(child, word, index + 1)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        for word in words:
            self.insert(word)
        self.count = 0
        curr = self.root
        self.dfs(curr,s,0)
        return self.count
