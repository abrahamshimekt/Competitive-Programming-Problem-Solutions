class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # if we have k odd numbers, the sum of their remainder after devide by
        # two is k
        # so the problem can be converted to the number of subarrays whose 
        # remainder sum up to k thus because the remainders are either 0 or 1
        # so only the ones will contribute to the sum up to k
    
        N = len(nums)

        remainder_prefix = []
        
        remainder = 0

        for num in nums:

            remainder += num%2

            remainder_prefix.append(remainder)

        remainders = defaultdict(int,{0:1})

        num_subarrays = 0

        for index in range(N):

            if remainder_prefix[index]-k in remainders:
                
                num_subarrays += remainders[remainder_prefix[index]-k]

            remainders[remainder_prefix[index]] +=1

        return num_subarrays




        