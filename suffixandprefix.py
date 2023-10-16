class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.indexes = []

class WordFilter:
    def __init__(self, words: List[str]):
        self.prefixRoot = TrieNode()
        self.suffixRoot = TrieNode()
        for i in range(len(words)):
            self.insert(words[i], self.prefixRoot, i)
            self.insert(words[i][::-1], self.suffixRoot, i)
        
            

    def insert(self, word, root, i):
        curr = root

        for c in word:
            index = ord(c)-97
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.indexes.append(i)

    def searchPrefix(self, prefix, root):
        curr = root
        for c in prefix:
            index = ord(c)-97
            if  not curr.children[index]:
                return set()
            curr = curr.children[index]
        return curr.indexes

    def f(self, pref: str, suff: str) -> int:
        prefixes = self.searchPrefix(pref, self.prefixRoot)
        suffixes = self.searchPrefix(suff[::-1], self.suffixRoot)
        i = len(prefixes)-1
        j = len(suffixes)-1
        while i >=0 and j >=0:
            if prefixes[i] == suffixes[j]:
                return prefixes[i]
            elif prefixes[i] > suffixes[j]:
                i -=1
            else:
                j -=1
        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref, suff)
