class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_subarrays = 0
        currsum =0
        prefixsum= {0:1}
        for num in nums:
            currsum +=num
            diff = currsum -k
            num_subarrays += prefixsum.get(diff,0)
            prefixsum[currsum] = 1 + prefixsum.get(currsum,0)
        return  num_subarrays
        