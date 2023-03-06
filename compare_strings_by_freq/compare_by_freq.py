class Solution:
    def word_freq(self,word):
        freq = defaultdict(int)
        smallest = 'z'
        for char in word:
            freq[char] +=1
            if char < smallest:
                smallest = char
        return freq[smallest]
    def search(self,query,words):
        left = -1
        right = len(words)
        
        while right -left > 1:
            mid = left + (right-left)//2
            if words[mid] > query:
                right = mid
            else:
                left = mid
        return right

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        for index in range(len(words)):
            words[index] = self.word_freq(words[index]) 

        words.sort()

        for indxx in range(len(queries)):
            queries[indxx] = self.word_freq(queries[indxx])

        answer  = []

        for query in queries:
            index = self.search(query,words)
            answer.append(len(words)-index)
        return answer


        
        



        