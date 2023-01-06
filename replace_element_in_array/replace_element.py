class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_index = {}
        for index,num in enumerate(nums):
            nums_index[num] = index
        
        for operation in operations:

            replaced_num_index = nums_index[operation[0]]
            nums[replaced_num_index] =operation[1]
            nums_index[operation[1]] = replaced_num_index
            
        return nums 
