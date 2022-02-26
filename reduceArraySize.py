from ast import List
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr)//2
        num_occur = Counter(arr)
        sorted(num_occur.values(), reverse=True)
        total = 0
        count = 0
        for num in num_occur:
            total += num
            count +=1
            if total >= half:
                return count