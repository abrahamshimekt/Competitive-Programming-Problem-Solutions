def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabets = {}
        for index,ch in enumerate(order):
            alphabets[ch] = index
        words_list = []
        for word in words:
            word_cur = []
            for i in range(len(word)):
                word_cur.append(alphabets[word[i]])
            words_list.append(word_cur)
        for j in range(len(words_list)-1):
            if words_list[j] > words_list[j+1]:
                return False
        return True