class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            if freq.get(num,0) >1:
                return True
            else:
                freq[num] =1
        return False