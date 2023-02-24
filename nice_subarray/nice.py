class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        remainders = []
        rem = 0
        num_subarray = 0
        for num in nums:
            rem += num % 2
            remainders.append(rem)
        prefix = {0: 1}
        for remainder in remainders:
            if remainder - k in prefix:
                num_subarray += prefix[remainder - k]
            if remainder not in prefix:
                prefix[remainder] =1
            else:
                prefix[remainder] += 1
        return num_subarray

                