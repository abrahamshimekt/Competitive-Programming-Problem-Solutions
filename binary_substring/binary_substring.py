class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int,{0:1})
        curr_sum = 0
        num_binary_sub_array = 0
        # the idea of solving this problems is to find two prefix sum where the difference between them 
        # gives the goal specified for the given test case
        # so we need to find that a -b = goal where a and b are two prefix sums same as a-goal = b
        # so we need to search for b in the prefix array

        for index in range(len(nums)):

            curr_sum += nums[index]
            if curr_sum - goal in prefix:
                num_binary_sub_array += prefix[curr_sum - goal]
                
            prefix[curr_sum] +=1

        return num_binary_sub_array