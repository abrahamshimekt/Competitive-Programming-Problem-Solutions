class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] =1
            else:
                freq[num] +=1
        count = 0
        for num_ in nums:
            if freq[num_] >0 and freq.get(k-num_,0) > 0:
                if k-num_ == num_:
                    if freq.get(k-num_) > 1:
                        count +=1
                        freq[k-num_] -=1
                        freq[num_] -=1
                else:
                    count +=1
                    freq[k-num_] -=1
                    freq[num_] -=1
        return count

        