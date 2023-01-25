from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        count =0
        for num in nums:
            if freq.get(k - num,0) >0 :
                freq[k-num] -=1
                count +=1
            else:
                freq[num] +=1
        return count