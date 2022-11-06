class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_ = Counter(words1)
        words2_ = Counter(words2)
        count = 0
        for word in words1_:
            if word in words2_:
                if words1_[word] == words2_[word] ==1:
                    count +=1
        return count