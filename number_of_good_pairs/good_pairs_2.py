 def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] =1
            else:
                freq[num] +=1
        pairs =0
        for n in freq:
            if freq[n] >1:
                pairs += (freq[n]*(freq[n]-1))//2
        return pairs