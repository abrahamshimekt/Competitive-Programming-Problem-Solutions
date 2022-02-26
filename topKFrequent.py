from ast import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedNum= sorted(Counter(nums).items(), key = lambda x:x[1], reverse = True)
        outPut =[]
        for i in range(k):
            outPut.append(sortedNum[i][0])
        return outPut