from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for word in words:
           freq[word]-=1
        heap = []
       
        for word in freq:
           
            heapq.heappush(heap,[freq[word],word])
            
        topFrequent = []
        for index in range(k):
            word = heapq.heappop(heap)
            topFrequent.append(word[1])

        return topFrequent

        

