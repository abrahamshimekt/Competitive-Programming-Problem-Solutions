class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int,{0:1})
        curr_sum = 0
        num_sub = 0
        for index in range(len(nums)):
            curr_sum += nums[index]
            if curr_sum-k in prefix:
                num_sub += prefix[curr_sum-k]
            prefix[curr_sum] +=1
        return num_sub
            

        


        