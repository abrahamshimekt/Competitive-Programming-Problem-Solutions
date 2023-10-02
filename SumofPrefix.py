class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.count += 1

    def searchPrefix(self, word):
        curr = self.root
        count = 0
        for c in word:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
            count += curr.count
        return count

    def sumPrefixScores(self, words):
        answer = []

        for word in words:
            self.insert(word)

        for word in words:
            count = self.searchPrefix(word)
            answer.append(count)
        return answer
