def similarPairs(self, words: List[str]) -> int:
        pairs = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if set(words[i]) == set(words[j]):
                    pairs +=1
        return pairs
        # words_dict = {}
        # for word in words:
        #     word = ''.join(set(word))
        #     if word not in words_dict:
        #         words_dict[word] =1
        #     else:
        #         words_dict[word] +=1
        # pairs = 0
        # print(words_dict)
        # for w in words_dict:
        #     if words_dict[w] > 1:
        #        pairs += (words_dict[w]*(words_dict[w]-1))//2
        # return pairs