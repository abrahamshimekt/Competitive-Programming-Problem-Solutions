class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOf = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.root.isEndOf = True

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOf = True

    def backTrack(self, curr, path):
        if not curr.isEndOf:
            
            word = "".join(path[:-1])
            currLength = len(path)-1
            if currLength > self.maxLength:
                self.maxLength = currLength
                self.answer = [word]
            elif currLength == self.maxLength:
                self.answer.append(word)
            return
        if not curr.children:
            word = "".join(path)
            currLength = len(path)
            if currLength >self.maxLength:
                self.maxLength = currLength
                self.answer = [word]
            elif currLength == self.maxLength:
                self.answer.append(word)
            return

        for child in curr.children:
            path.append(child)
            self.backTrack(curr.children[child], path)
            path.pop()

    def longestWord(self, words):
        for word in words:
            self.insert(word)
        self.answer = []
        self.maxLength = 0
        curr = self.root

        self.backTrack(curr, [])
        self.answer.sort()

        return self.answer[0]
