class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        mask = [0]*N
        for index in range(N):
            for char in words[index]:
                mask[index] |= 1<< (ord(char)-ord("a"))
        product_word_length = 0
        for index_i in range(N):
            for index_j in range(index_i+1,N):
                if mask[index_i] & mask[index_j] == 0:
                    product_word_length = max(product_word_length,len(words[index_i])*len(words[index_j]))
        return product_word_length